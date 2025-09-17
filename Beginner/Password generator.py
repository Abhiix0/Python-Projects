import random
import string
from datetime import datetime

def generate_password(length):
    if length < 4:
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
        
