import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    # Character sets
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate password
    return ''.join(random.choice(char_pool) for _ in range(length))

def main():
    print("Random Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return
        
        use_letters = input("Include letters? (yes/no): ").lower() == "yes"
        use_numbers = input("Include numbers? (yes/no): ").lower() == "yes"
        use_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception:
        print("An unexpected error occurred.")

if __name__ == "__main__":
    main()
