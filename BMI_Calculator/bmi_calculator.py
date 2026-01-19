#BMI_Calculator

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100        # cm to meter
    bmi_value = weight_kg / (height_m ** 2)
    return round(bmi_value, 2)


def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


print("===== Welcome to My BMI Calculator =====")

weight_input = float(input("Enter your body weight in kg: "))
height_input = float(input("Enter your height in cm: "))

bmi_result = calculate_bmi(weight_input, height_input)
status = bmi_status(bmi_result)

print("\nYour BMI Score is:", bmi_result)
print("Health Status:", status)
print("Take care of your health 🙂")
