# Take input from the user
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")


# Print even numbers between 1 and 20 using a for loop and if statement
print("Even numbers between 1 and 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

# Initialize variables
total = 0

# Take input from the user
number = float(input("Enter a number (enter 0 to stop): "))

# Calculate the sum using a while loop
while number != 0:
    total += number
    number = float(input("Enter a number (enter 0 to stop): "))

# Print the sum
print("The sum is:", total)


# Define the correct PIN
correct_pin = "1234"

# Ask the user for their PIN
pin = input("Enter your PIN: ")

# Check if the PIN is correct
if pin == correct_pin:
    print("Welcome to the ATM.")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Balance")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Withdrawal")
    elif choice == 2:
        print("Deposit")
    elif choice == 3:
        print("Balance")
    else:
        print("Invalid choice")
else:
    print("Incorrect PIN. Please try again.")
# Ask the user for username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Check if username and password are correct
if username == "admin" and password == "password123":
    print("Login successful")
else:
    print("Login failed. Incorrect username or password.")
