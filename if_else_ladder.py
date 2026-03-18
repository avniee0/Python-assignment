percentage = int(input("Enter your percentage: "))

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 75:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
elif percentage >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")