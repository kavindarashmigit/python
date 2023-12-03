# Initialize variables
total = 0
number = 20

# Input numbers until -999 is entered
while number != -999:
    try:
        number = float(input("Enter a number (-999 to terminate): "))
        if number != -999:
            total += number
    except ValueError:
        print("Please enter a valid number.")

# Print the sum of the numbers
print(f"Sum of the entered numbers: {total}")
