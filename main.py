import random

def generate_password(length: int) -> str:

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    special = "!@#$%^&*()+?><:{}[]"

    all_chars = lower_case + upper_case + numbers + special

    mandatory = [
        random.choice(upper_case),
        random.choice(numbers)
    ]

    password = [random.choice(all_chars)  for i in range(length - len(mandatory)) ]

    password.extend(mandatory)
    random.shuffle(password)

    return "".join(password)



password = generate_password(5)
print(password)