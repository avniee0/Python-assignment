age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))

if age >= 18:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible (weight should be at least 50 kg).")
else:
    print("You are not eligible")