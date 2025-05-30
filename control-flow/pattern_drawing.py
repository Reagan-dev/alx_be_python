# pattern_drawing.py
size_pattern = int(input("Enter the size of the pattern: "))

# draw the pattern
row = 0

# Use a while loop for rows
while row < size_pattern:
    # Use a for loop for columns
    for col in range(size_pattern):
        print("*", end="")  # print stars in the same row
    print()  # move to the next line after each row
    row += 1