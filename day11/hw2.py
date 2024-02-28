# Prompt the user for their age
age = int(input("Please enter your age: "))

# Check the age range and print the appropriate message
if age < 0:
    print("Invalid age entered.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
