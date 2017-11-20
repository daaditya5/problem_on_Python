""" this program will gives the output whether the input is leap year or not """

def leap_year():
    year = int(input("please enter the year = "))
    if year % 4 != 0:
        print(year, "is not leap year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print(year, "is leap year")
        else:
            print(year, "is not leap year")
    else:
        print(year, "is leap year")


leap_year()