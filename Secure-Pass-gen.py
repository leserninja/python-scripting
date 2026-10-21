import string
import random
import time
import sys
import os


#NOTE: Restricted to linux and macOS at the moment, but partially works on Windows as well, just cant save passwords.


def generate_password(length):
    characters = (
        string.ascii_lowercase
        +string.ascii_uppercase
        +string.digits
        +string.punctuation
    )
        
    password_char = [random.choice(characters) for _ in range(length)]
    return "".join(password_char)

# runs a loop of if gen erated password is less than 8 characters or more than 50 characters, it will ask for a new length until a valid length is provided and else it will generate a password and ask if the user wants to save it to a file, if yes it will save it to Downloads folder or home directory depending on if Downloads folder exists or not.
while True:
    if __name__ == "__main__":
        print("\nWelcome to the Secure Password Generator!\nAll Your passwords will be saved in a file named 'Generated_passwords.txt' in your Downloads folder or home directory if Downloads folder does not exist.\n")
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

# says first to make Downloads folder deafualt then checks if it exists, if not then saves to home directory
# might be a conflict if the user already has a file named passwords.txt in either Downloads or home directory, but it will just append to the file if it exists.
                save_path = os.path.join(os.path.expanduser("~/Downloads") if os.path.exists(os.path.expanduser("~/Downloads")) else os.path.expanduser("~"), "Generated_passwords.txt")
                save_pass = input("Do you want to save this password to a file? (y/n): ").strip().lower()
                if save_pass == "y":
                    with open(save_path, "a") as file:
                        file.write(f"{secure_password}\n")
                    print("Your password has been saved with the name 'Generated_passwords.txt'. at either your Downloads folder  or home directory .")
                    break
                elif save_pass == "n":
                    print("Your password has not been saved.")
                    break            
        except ValueError:
            print("Please enter a valid integer for the password length.")
            time.sleep(0.5)


