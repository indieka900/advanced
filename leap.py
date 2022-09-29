year = int(input("Enter a year to check: "))
if year % 4 == 0 and year % 2==0:
    print("Is a leap year")
else:
    print("Not a leap year")