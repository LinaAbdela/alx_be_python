# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use while loop to iterate through each row
while row < size:
    # Use for loop to print asterisks side by side in the current row
    for _ in range(size):
        print("*", end="")
    # After printing one row, move to the next line
    print()
    # Increment the row counter
    row += 1
