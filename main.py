import streamlit as st
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from app.generate_pdf import generate_student_pdf
from app.image_converter import convert_pdf_to_images
from app.send_whatsapp import send_whatsapp_with_image
import pandas as pd
import os
from database import find_user_by_email, create_user, verify_password

# Paths for outputs
PDF_FOLDER = "app/output_pdfs"
IMAGE_FOLDER = "app/output_images"
POPPLER_PATH = r'C:\Program Files\poppler-23.11.0\Library\bin'

# Streamlit Pages


# Function to load HTML from a file
def load_page():
    # Load the HTML page content
    with open(os.path.join("templates", "index.html"), "r") as f:
        html_content = f.read()
    st.markdown(html_content, unsafe_allow_html=True)

    # Include the CSS file for styling
    with open(os.path.join("static", "styles.css"), "r") as f:
        css_content = f.read()
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

    # Include the JS file for interactivity
    with open(os.path.join("static", "script.js"), "r") as f:
        js_content = f.read()
    st.markdown(f"<script>{js_content}</script>", unsafe_allow_html=True)

# Streamlit page setup
st.set_page_config(page_title="AutoRiz", page_icon=":guardsman:", layout="centered")

# Load the UI and wait for the animation to complete
load_page()

def login_page():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = find_user_by_email(email)  # Fetch user from DB
        if user and verify_password(user["password"], password):  # Check password validity
            st.session_state['logged_in'] = True
            st.session_state['user'] = user
            st.success("Login successful!")
            st.experimental_rerun()
        else:
            st.error("Invalid email or password.")

def register_page():
    st.title("Register")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if find_user_by_email(email):  # Check if email already exists
            st.error("Email already registered.")
        else:
            create_user(name, email, password)  # Create new user in DB
            st.success("Registration successful! Please log in.")
            st.session_state['page'] = 'login'
            st.experimental_rerun()

def upload_page():
    st.title("Upload Excel File")
    uploaded_file = st.file_uploader("Upload Excel File", type=['xlsx'])

    if uploaded_file:
        st.info("Processing started. Please wait...")
        df = pd.read_excel(uploaded_file)

        os.makedirs(PDF_FOLDER, exist_ok=True)
        os.makedirs(IMAGE_FOLDER, exist_ok=True)

        pdf_paths = []

        for _, row in df.iterrows():
            student_data = row.to_dict()
            pdf_path = generate_student_pdf(student_data, PDF_FOLDER)
            pdf_paths.append((pdf_path, student_data["Contact"], student_data["USN"]))
            st.success(f"PDF created for {student_data['Name']} (USN: {student_data['USN']})")

        image_paths_dict = {}
        for pdf_path, contact, usn in pdf_paths:
            image_paths = convert_pdf_to_images(pdf_path, IMAGE_FOLDER, POPPLER_PATH)
            image_paths_dict[contact] = image_paths
            st.success(f"Images created for USN: {usn}")

        for contact, image_paths in image_paths_dict.items():
            for image_path in image_paths:
                result = send_whatsapp_with_image(contact, image_path)
                if result is not True:
                    st.error(f"Error sending to {contact}: {result}")
                else:
                    st.success(f"Report sent to {contact}")

        st.balloons()
        st.success("All processes completed successfully!")
    
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.experimental_rerun()

# Main Navigation
if "logged_in" not in st.session_state:
    st.session_state['logged_in'] = False

if "page" not in st.session_state:
    st.session_state['page'] = "login"

if st.session_state['logged_in']:
    upload_page()
else:
    if st.session_state['page'] == "login":
        login_page()
    elif st.session_state['page'] == "register":
        register_page()

if st.button("Switch to Register/Login"):
    st.session_state['page'] = "register" if st.session_state['page'] == "login" else "login"
    st.experimental_rerun()
