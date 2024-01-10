def validate_password(password):
    # Check length
    if not 8 <= len(password) <= 16:
        return False

    # Check character classes without using re
    uppercase_count = sum(1 for char in password if char.isupper())
    lowercase_count = sum(1 for char in password if char.islower())
    number_count = sum(1 for char in password if char.isdigit())

    if uppercase_count < 2 or lowercase_count < 2  or number_count < 2:
        return False

    # If all checks pass, the password is valid
    return True

# Example usage:
password = "StrongP@ssw0r2ed"
if validate_password(password):
    print("Password is valid.")
else:
    print("Password does not meet complexity requirements.")