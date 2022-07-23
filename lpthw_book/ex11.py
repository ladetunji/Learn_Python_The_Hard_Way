print("Do you want to take this quiz?\nAnswer Yes (y) or No (n)")
answer = input()
name = input("What is your name? ")
print("How old are you?", end = ' ')
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weigh?", end = ' ')
weight = input()
print(f"""
You responded \"{answer}\" to the quiz.
Your name is {name}, you are {age} years old, {height} tall and {weight} heavy.
""")
