# call argunent variable from system
from sys import argv
# Save 2 arguments in argv for "script name" and "filename" you wish to work on
script = argv

# set variable txt to open filename variable
print("Type the name of the file you wish to open")
filename = input("> ")
txt = open(filename)

# print text with f-string
print(f"Here's your file {filename}:")
# print to read text from filename
print(txt.read())
print(txt.close())
# print to repeat the process again
# print("Type the filename again:")
# set new variable file-again to receive user input
# file_again = input("> ")
# set variable text-again to open fiename from user input
# txt_again = open(file_again)
# print to read filename again
# print(txt_again.read())
