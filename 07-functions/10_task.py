import random
import string

# ! Not Recommended
# def password_generator(len: int = 10):
#     letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     numbers = "0123456789"
#     symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

#     chars = letters + numbers + symbols

#     pwd = ''

#     for i in range(len):
#         idx = (i * 7 + 3) % len(chars)
#         pwd += chars[idx]

#     return pwd


def password_generator(len: int = 10):
    chars = string.ascii_letters + string.digits + string.punctuation
    chars = list(chars)

    random.shuffle(chars)

    randomized_chars = "".join(chars)

    pwd = random.choices(randomized_chars, k=len)
    pwd = "".join(pwd)
    return pwd


len = int(input("What length do you want for your password? "))

gen_pwd = password_generator(len=len)

print(f"Your generated password is: {gen_pwd}")
