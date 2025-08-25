user_year = int(input("Enter your year: "))

if user_year % 4 == 0:
    if user_year % 100 == 0:
        if user_year % 400 == 0:
            print(f"{user_year} is a leap year.")
        else:
            print(f"{user_year} is not a leap year.")
    else:
        print(f"{user_year} is not a leap year.")
else:
    print(f"{user_year} is not a leap year.")

