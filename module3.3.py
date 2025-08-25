user_gender = input("Enter your gender: M for male, F for female\n")
user_gender = user_gender.upper()

if user_gender == "M":
    male_hemoglobin = float(input("Enter your hemoglobin value in g/l: "))
    if 134 <= male_hemoglobin <= 167:
        print("You are healthy. It is normal.")
    elif male_hemoglobin > 167:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is low.")
elif user_gender == "F":
    female_hemoglobin = float(input("Enter your hemoglobin value in g/l: "))
    if 117 <= female_hemoglobin <= 155:
        print("You are healthy. It is normal.")
    elif female_hemoglobin > 155:
        print("Your hemoglobin is high.")
    else:
        print("Your hemoglobin is low.")
else:
    print("Invalid input. Try again.")


