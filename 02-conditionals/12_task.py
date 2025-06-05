# Evaluate potential applicant on Python knowlege for HR team
import math

name = input("Insert your name: ")
years_of_experience = input("How many years of experience do you have: ")
skills = input("What are your skills? ")

years_of_experience = float(years_of_experience)
years_of_experience = math.floor(years_of_experience)

skills = skills.split(",")
skills = [s.strip().lower() for s in skills]

knows_python = "python" in skills or "django" in skills

result = ""

if knows_python and years_of_experience >= 3:
    result = "Optimal candidate."
elif knows_python and years_of_experience >= 1:
    result = "Good candidate."
elif knows_python:
    result = "Possible candidate."
else:
    result = "No elegible for the job!"

print(result)
