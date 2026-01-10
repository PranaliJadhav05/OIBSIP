print("----- BMI CALCULATOR -----")

try:
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))

    if weight <= 0 or height <= 0:
        print("Please enter valid positive values.")
    else:
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        print("\nYour BMI is:", bmi)

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 25:
            print("Category: Normal weight")
        elif bmi < 30:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Invalid input! Please enter numbers only.")
