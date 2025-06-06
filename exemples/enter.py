from pratik import enter


print("\n# Prompt the user to enter an integer")
number = enter("Enter an integer: ", int)
print(f"You entered integer: {number}")


print("\n# Prompt the user to enter a boolean value")
response = enter("Do you agree? (yes/no): ", bool)
print(f"Boolean response: {response}")


print("\n# Prompt the user to enter a list of numbers")
numbers = enter("Enter a list of numbers (spaces-separated): ", list)
print(f"You entered list: {numbers}")


print("\n# Prompt the user to enter a complex number")
complex_num = enter("Enter a complex number (e.g., 1+2j): ", complex)
print(f"You entered complex number: {complex_num}")


print("\n# Prompt the user to enter a slice")
slicing = enter("Enter a slice (e.g., 1:5): ", slice)
print(f"You entered slice: {slicing}")


print("\n# Handle invalid input with a retry loop")
try:
    percentage = enter("Enter a float percentage (0.0 - 100.0): ", float)
    if not (0 <= percentage <= 100):
        raise ValueError("Percentage must be between 0 and 100.")
    print(f"Valid percentage: {percentage}")
except ValueError as e:
    print(f"Error: {e}")
