import string
import random
import time

def generate_password(length):
    characters = (
        string.ascii_lowercase
        +string.ascii_uppercase
        +string.digits
        +string.punctuation
    )
        
    password_char = [random.choice(characters) for _ in range(length)]
    return "".join(password_char)

while True:
    if __name__ == "__main__":
        print("Welcome to the Secure Password Generator!")
        try:
            user_length = int(
                input("Enter the desired password length (minimum 8 characters): ")
            )
            if user_length < 8:
                print("Your password length must be at least 8 characters.")
                time.sleep(0.5)
            elif user_length > 50:
                print("Your password length must be at most 50 characters.")
                time.sleep(0.5)
            else:
                secure_password = generate_password(user_length)
                print(f"\nYour secure password is:\n{secure_password}")
                break            
        except ValueError:
            print("Please enter a valid integer for the password length.")
            

