# This is to deal with exceptions in inputs and other unexpected scenarios
x = int(input("x= "))
y = int(input("y= "))
if y != 0:
    result = x / y
    print(f"The division of {x} by {y} equals {result}.\n")
else:
    print("You should not input y as zero!\n")