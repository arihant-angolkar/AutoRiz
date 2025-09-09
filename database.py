import re
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

# MongoDB Setup
MONGO_URI = "mongodb://localhost:27017"  # Replace with Atlas URI if needed
client = MongoClient(MONGO_URI)
db = client['user_database']
users_collection = db['users']

def find_user_by_email(email):
    """Find a user by their email."""
    return users_collection.find_one({"email": email})

def find_user_by_username(username):
    """Find a user by their username."""
    return users_collection.find_one({"name": username})

def create_user(name, email, password):
    """Create a new user."""
    # Check if the email is in a valid format
    if not is_valid_email(email):
        raise ValueError("Invalid email format.")
    
    # Check if the password has at least 8 characters
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    
    # Check if the username is unique
    if find_user_by_username(name):
        raise ValueError("Username already exists.")

    # Hash the password before storing
    hashed_password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
    users_collection.insert_one({"name": name, "email": email, "password": hashed_password})

def verify_password(stored_password, input_password):
    """Verify if the input password matches the stored hashed password."""
    return check_password_hash(stored_password, input_password)

def is_valid_email(email):
    """Check if the email is in a valid format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))
