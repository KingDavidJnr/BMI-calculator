# A program that collect inputs from users
# Collects their names
# Collects their weight as int
# Take their height as float values
# Calculates and output their body mass index
# With a personalized message

your_name = input("Enter your name: ")
your_age = input("Enter your age: ")
your_weight = input("Enter your weight(in KG): ")
your_height = float(input("Enter your height(in Metres): "))

weight = int(your_weight)

# A program that calculates Body-Mass_Index of its users
body_mass_index = (weight / (your_height ** 2.0))
print("Your BMI is", body_mass_index)

if body_mass_index < 18.5:
    print(your_name + ", you\'re underweight")
elif body_mass_index >= 18.5 and body_mass_index <= 24.9:
    print(your_name + ", you\'re within the Healthy Weight range")
elif body_mass_index >= 25.0 and body_mass_index <= 29.9:
    print(your_name + ", you\'re overweight")
else:
    print(your_name + ", you\'re obese")