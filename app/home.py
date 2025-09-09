import streamlit as st

# Define function to show EC or CS pages based on selection
def show_field_page(field):
    if field == "EC":
        st.write("You selected EC. Now showing EC PGs...")
        # You can display more EC-related content here
        st.write("List of EC PGs will appear here...")
    elif field == "CS":
        st.write("You selected CS. Now showing CS PGs...")
        # You can display more CS-related content here
        st.write("List of CS PGs will appear here...")

def main():
    # Display the main page title after the animation
    st.markdown("<h1 style='text-align: center;'>AutoRiz</h1>", unsafe_allow_html=True)
    
    # Add a title to the Streamlit page
    st.markdown("### Please choose your field:")

    # Radio button for EC and CS selection
    selected_field = st.radio(
        "Choose a field:",
        ["EC", "CS"]
    )
    
    # Call function to show field-specific content based on selection
    show_field_page(selected_field)

    # You can use buttons or further navigation to go to the main page
    if st.button("Go to Main Page"):
        st.title("Welcome to the Main Page")
        st.write("Here is the main content for your AutoRiz application.")

if __name__ == "__main__":
    main()
import streamlit as st

# Define function to show EC or CS pages based on selection
def show_field_page(field):
    if field == "EC":
        st.write("You selected EC. Now showing EC PGs...")
        # You can display more EC-related content here
        st.write("List of EC PGs will appear here...")
    elif field == "CS":
        st.write("You selected CS. Now showing CS PGs...")
        # You can display more CS-related content here
        st.write("List of CS PGs will appear here...")

def main():
    # Display the main page title after the animation
    st.markdown("<h1 style='text-align: center;'>AutoRiz</h1>", unsafe_allow_html=True)
    
    # Add a title to the Streamlit page
    st.markdown("### Please choose your field:")

    # Radio button for EC and CS selection
    selected_field = st.radio(
        "Choose a field:",
        ["EC", "CS"]
    )
    
    # Call function to show field-specific content based on selection
    show_field_page(selected_field)

    # You can use buttons or further navigation to go to the main page
    if st.button("Go to Main Page"):
        st.title("Welcome to the Main Page")
        st.write("Here is the main content for your AutoRiz application.")

if __name__ == "__main__":
    main()
