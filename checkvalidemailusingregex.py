import re

def is_valid_email(email):
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # matching check
    if re.match(pattern, email):
        return True
    return False


print(is_valid_email("user@domain.com"))  #  True
print(is_valid_email("user@domain"))     # False
