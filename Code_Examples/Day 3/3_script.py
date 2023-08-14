def calculate_bmi(height=0, weight=0):
    if height == 0:
        height = float(input("Enter height in meters: "))
    if weight == 0:
        weight = float(input("Enter weight in kilograms: "))

    bmi = weight / (height ** 2)
    return bmi

bmi = calculate_bmi()
print(f"Your BMI is: {bmi:.2f}")