my_name = 'Ladetunji Osibanjo'
my_age = 36 # not a lie
my_height = 76 # inches
my_height_cm = my_height * 2.54
my_weight = 230 # lbs
my_weight_kg = my_weight / 2.2046
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Dark Brown'

print(f"Let's talk about Mr. {my_name}.")
print(f"He's {my_height} inches tall.")
print("That's about", round(my_height_cm), "centimetres tall, for the UK audience.")
print(f"He's {my_weight} pounds heavy.")
print("That's about", round(my_weight_kg), "kilograms heavy, for the UK audience.")
print(f"If he were in the UFC, he'd be a Heavyweight.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} when he's not had coffee.")

# This line is tricky, try to get it exactly right.

total = my_age + my_weight + my_height
total2 = my_age + my_weight_kg + my_height_cm
print(f"If I add {my_age}, {my_weight} and {my_height}, I get {total}.")
print(f"If I ran the sum a second time with {my_age}, {my_weight_kg}, and {my_height_cm}, the total would be {total2}.")
