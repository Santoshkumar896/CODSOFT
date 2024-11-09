import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the user specifies a valid length
    if length < 4:
        print("Password length should be at least 4 for a secure password.")
        return None
    
    # Randomly select characters from the character pool to create a password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    print("Password Generator")
    
    # Prompt the user for password length
    try:
        length = int(input("Enter the desired password length: "))
        
        # Generate password
        password = generate_password(length)
        
        # Display the generated password
        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number for the password length.")

# Run the password generator
main()
