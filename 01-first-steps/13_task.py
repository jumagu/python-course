name = input("What is your name? ")
year_of_birth = input("What is your year of birth? ")
email = input("What is your email? ")
password = input("What is your password? ")

future_age = 2050 - int(year_of_birth)
formatted_pwd = len(password) * "*"

result = f"""
Name: {name}
Email: {email}
You will be {future_age} in 2050
Youe password is: {formatted_pwd}
"""

print(result)
