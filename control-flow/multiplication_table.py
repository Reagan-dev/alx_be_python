# multiplication table generator
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1, 11):
    x = number
    y = i
    product = x * y
    # Print the multiplication table
    print(f"{x} x {y} = {product}")
    print()
    i += 1
      
