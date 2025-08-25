user_cabin_class = input("Enter your cabin class name: ")
user_cabin_class = user_cabin_class.upper()

if user_cabin_class == "LUX":
    print("upper-deck cabin with a balcony")
elif user_cabin_class == "A":
    print("above the car deck, equipped with a window")
elif user_cabin_class == "B":
    print("windowless cabin above the car deck")
elif user_cabin_class == "C":
    print("windowless cabin below the car deck")
else:
    print("Invalid cabin class")


