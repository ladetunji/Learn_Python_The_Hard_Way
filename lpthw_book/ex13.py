from sys import argv
# Read the WYSS section for how to run this
script, first, middle, last, age, ageIn2 = argv
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

first = input("What is your first name? ")
middle = input("What is your middle name? ")
last = input("What is your last name? ")
age = int(input("How old are you? "))
ageIn2 = age + 2

print(f"""The script is called {script}.
Your full name is {first} {middle} {last}.
You are {age} years old today, but in 2 years time you will be {ageIn2} years old.""")
