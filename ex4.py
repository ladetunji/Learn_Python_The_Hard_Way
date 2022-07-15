# Set a variable to denote the number of cars
cars = 100
# Set a variable to denote the number of available seats in a car
space_in_a_car = 4.0
# Set a variable to denote the number of drivers
drivers = 30
# Set a variable to denote the number of passengers
passengers = 90
# Calculate the number of empty cars on the day
cars_not_driven = cars - drivers
# Calculate the number of working cars on the day
cars_driven = drivers
# Calculate the number of available seating capacity in all working cars
carpool_capacity = cars_driven * space_in_a_car
# Calculate the number of average passengers who can ride in the cars
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car")
