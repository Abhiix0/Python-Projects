<<<<<<< HEAD
import random
import string
=======
import string
import random
>>>>>>> 822e1c065e0eaf25f5dc6d1aec8757bbe9daad50
from datetime import datetime

def generate_password(length):
    if length < 4:
<<<<<<< HEAD
        raise ValueError("Password length should be at least 4 characters.")
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        guaranteed = [random.choice(lower), random.choice(upper), random.choice(digits), random.choice(symbols)]
        all_characters = lower + upper + digits + symbols
        rest = [secrets.choice(all_chars) for _ in range(length - 4)]
        password_list = guaranteed + rest
        random.systemrandom().shuffle(password_list)
        password = ''.join(password_list)
        return password
        
=======
        raise ValueError("Password length must be at least 4")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return "".join(password)

def save_password(password):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("saved_passwords.txt", "a") as f:
        f.write(f"{ts} - {password}\n")

if __name__ == "__main__":
    n = int(input("Password length? "))
    pwd = generate_password(n)
    print("Generated:", pwd)
    save_password(pwd)
    print(" Saved to saved_passwords.txt")
>>>>>>> 822e1c065e0eaf25f5dc6d1aec8757bbe9daad50
