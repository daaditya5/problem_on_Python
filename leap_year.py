def leap_year(year):
    """ this program will gives the output whether the input is leap year or not """
    if year % 4 != 0:
        print(year, "is not leap year")
    elif year % 100 == 0:
        if year % 400 == 0:
            print(year, "is leap year")
        else:
            print(year, "is not leap year")
    else:
        print(year, "is leap year")


while True:
    inp_year = input("please enter the year = ")
    if inp_year == 'done':
        break
    else:
        year = int(inp_year)
        leap_year(year)