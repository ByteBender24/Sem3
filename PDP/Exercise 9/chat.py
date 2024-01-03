import json
import os
import re
from datetime import datetime

# User data storage
user_data_file = "user.json"
if not os.path.exists(user_data_file):
    with open(user_data_file, "w") as file:
        json.dump({}, file)

# Function for user registration


def register_user(username, password):
    # Validate username format
    if not re.match(r"^[a-zA-Z0-9_]{4,20}$", username):
        raise Exception("Invalid username")

    # Validate password format
    if not re.match(r"^(?=.[A-Za-z])(?=.\d)(?=.*[@#$%^&!])[A-Za-z\d@#$%^&!]{8,}$", password):
        raise Exception("Invalid password")

    with open(user_data_file, "r") as file:
        user_data = json.load(file)

        # Check if the username already exists
        if username in user_data:
            raise Exception("Username already exists")

    # Store user data
    user_data[username] = {"password": password}

    with open(user_data_file, "w") as file:
        json.dump(user_data, file)

# Function for user authentication


def authenticate_user(username, password):
    with open(user_data_file, "r") as file:
        user_data = json.load(file)

        # Check if the username exists and the password matches
        if username in user_data and user_data[username]["password"] == password:
            return True
        return False


# Message data storage
message_db = "message.json"
if not os.path.exists(message_db):
    with open(message_db, "w") as file:
        json.dump([], file)

# Function for sending a message


def send_message(sender, recipient, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message_data = {
        "sender": sender,
        "recipient": recipient,
        "timestamp": timestamp,
        "message": message,
    }
    with open(message_db, "r") as file:
        messages = json.load(file)
    messages.append(message_data)
    with open(message_db, "w") as file:
        json.dump(messages, file)

# Function for retrieving messages


def retrieve_messages(user):
    with open(message_db, "r") as file:
        messages = json.load(file)
    user_messages = [msg for msg in messages if msg["sender"]
                     == user or msg["recipient"] == user]
    return user_messages

# Function for searching messages


def search_messages(user, search_term):
    messages = retrieve_messages(user)
    found_messages = [msg for msg in messages if re.search(
        search_term, msg["message"])]
    return found_messages


# Sample usage
if __name__ == "__main__":
    try:
        register_user("user1", "password1")
    except Exception as e:
        print(e)

    if authenticate_user("user1", "password1"):
        print("Authentication successful")
    else:
        print("Authentication failed")

    send_message("user1", "user2", "Hello, user2!")
    send_message("user2", "user1", "Hi, user1!")
    user1_messages = retrieve_messages("user1")
    print("User1's messages:", user1_messages)

    # Search for messages
    search_results = search_messages("user1", r"Hi|Hello")
    print("Search results:", search_results)
