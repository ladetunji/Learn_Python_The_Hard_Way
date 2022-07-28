from sys import argv
script, user_name, location = argv
prompt = '> '

print(f"Hi {user_name}, from {location}. I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"\nDo you like me, {user_name}?")
likes = input(prompt)
print(f"Where do you live, {user_name}?")
lives = input(prompt)
print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said "{likes}" when I asked if you like me.
You live at {lives}, though I'm not sure where that is.
And you have a {computer} laptop.
Nice.""")
