import random
import string


def generate_otp_password():
    digits = random.choices(string.digits, k=4)
    return ''.join(digits)
