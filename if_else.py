num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greater number is:", num1)
    print("Smaller number is:", num2)
elif num2 > num1:
    print("Greater number is:", num2)
    print("Smaller number is:", num1)
else:
    print("Both numbers are equal")