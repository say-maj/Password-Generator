import random
import string

def generate_password(length=12):
    if length < 4:
        print("❌ Password length should be at least 4 characters.")
        return ""

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("=== 🔐 Password Generator ===")
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        password = generate_password(length)
        if password:
            print(f"\nYour secure password: \033[92m{password}\033[0m")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
