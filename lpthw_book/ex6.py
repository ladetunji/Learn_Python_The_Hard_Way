# Set a variable for types of people, assigned a value of 10
types_of_people = 10
# Set a variable x, assigned an f-string with a variable inside
x = f"There are {types_of_people} types of people."

# Set a variable binary, assigned a string binary
binary = "binary"
# Set a variable do_not, assigned a string don't
do_not = "don't"
# Set a variable y, assigned an f-string with variables inside
y = f"Those who know {binary} and those who {do_not}."

# Print variable x
print(x)
# Print variable y
print(y)

# Print 2 f-strings on new lines
print(f"I said: {x}.")
print(f"I also said: '{y}'.")

# Set variables boring or hilarious to boolean
boring = True
hilarious = False
# Set a variable joke_eval to a string with empty variable inside
joke_evaluation = "Isn't that joke so funny?! {} or {} or {}?"
# Print a string with a format(string)
print(joke_evaluation.format(boring, hilarious, "Cannot say"))

# Set 2 variables w and e with strings
w = "This is the left side of..."
e = " a string with a right side."
# Print a statement with 2 variables concatenated
print(w + e)

print("There were 4 places where a string was put inside another string.")

print("A longer string is formed because we concatenated 2 smallers strings together.")
