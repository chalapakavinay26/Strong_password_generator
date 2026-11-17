import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Strong Password Generator ---")
    length = int(input("password length (Length) enter (example 12): "))
    print(f"your new password: {generate_password(length)}")
