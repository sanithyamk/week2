import hashlib
user_data = {}
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in user_data:
        print("User already exists!")
    else:
        hashed_password = hash_password(password)
        user_data[username] = hashed_password
        print("Created new user")

def login(username, password):
    if username in user_data:
        if user_data[username] == hash_password(password):
            print("Login Successful")
        else:
            print("Invalid password")
    else:
        print("Username not found")

register("john", "mypassword")  
login("john", "mypassword")     
login("john1", "wrongpassword")  
