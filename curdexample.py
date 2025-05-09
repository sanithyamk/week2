def add_user(users, new_user):
    
    users.append(new_user)

def delete_user(users, user_id):
    
    users[:] = [user for user in users if user['id'] != user_id]

def update_user(users, user_id, updated_data):
    
    for user in users:
        if user['id'] == user_id:
            user.update(updated_data)
            return
    
def retrieve_user(users, user_id):

    for user in users:
        if user['id'] == user_id:
            return user
    return None

# Example usage:
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Add a new user
new_user = {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
add_user(users, new_user)
print("After adding new user:", users)

# Delete a user
delete_user(users, 2)
print("After deleting user:", users)

# Update a user
update_user(users, 1, {"name": "Alicia"})
print("After updating user:", users)

# Retrieve a user
retrieved_user = retrieve_user(users, 1)
print("Retrieved user:", retrieved_user)

retrieved_user = retrieve_user(users, 4)
print("Retrieved user (not found):", retrieved_user)