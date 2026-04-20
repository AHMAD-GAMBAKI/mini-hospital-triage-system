print("MINI HOSPITAL TRIAGE SYSTEM")

# input
name = input("Enter patient name: ")
age = int(input("Enter age: "))
has_id = input("Do you have hospital ID? (yes/no): ").lower()

weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

patient_id = int(input("Enter patient ID number: "))

# BMI(Body Mass Index) CALCULATION

bmi = weight / (height ** 2)

print("\n--- PATIENT REPORT ---")
print("Name:", name)
print("BMI:", round(bmi, 2))


# MODULO CHECK (ID VALIDATION)

if patient_id % 2 == 0:
    print("ID Status: Valid ")
else:
    print("ID Status: Invalid")


# ELIGIBILITY CHECK (LOGICAL OPERATORS)

if age >= 18 and has_id == "yes":
    print("\nStatus: Eligible for Assessment ")


    # NESTED IF (HEALTH CLASSIFICATION)

    if bmi < 18.5:
        print("Health Status: Underweight")
    elif bmi < 25:
        print("Health Status: Normal weight")
    elif bmi < 30:
        print("Health Status: Overweight")
    else:
        print("Health Status: Obese")

else:
    print("\nStatus: Not Eligible  (Age or ID issue)").


print("\nThank you for using MINI HOSPITAL SYSTEM ")