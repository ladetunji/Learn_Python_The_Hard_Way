# Print the nursery rhyme about Mary
print("Mary had a little lamb.")
# Print a string with enpty variable, then add a format string at the end
print("It's fleece was white as {}.".format("snow"))
print("And everywhere that Mary went.")
# Print a string multiplied by an integer to cause that string to repeat multiple times
print("." * 10) # What does that do?

# Assign strings of letters to variables
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch that comma at the end, try removing it to see what happens.
# Removing the comma at the end causes an error - you cannot define a variable in a concatenation without first ending the section with a comma. A plus does not work either.

print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# Printing a string multiple times by multiplying it to an integer, then concatenate to another string
print("tag, " * 5 + "end of tag")
