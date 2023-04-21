# Ask the user to input a year
year = int(input("Enter a year: "))

# Check if the year is within the Gregorian calendar period
if year < 1580:
    print("Not within the Gregorian calendar period")
# If the year is within the Gregorian calendar period, check if it is a common year or a leap year
else:
    # If the year is not divisible by 4, it is a common year
    if year % 4 !=0:
        print("Common year")
    # If the year is divisible by 4, check if it is divisible by 100 and 400 to determine if it is a leap year
    elif year % 100 !=0:
        print("Leap year")
    elif year % 400 !=0:
        print("Common year")
    else:
        print("Leap year")
