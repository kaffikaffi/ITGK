from itertools import cycle
weekdays = [
    "mon",
    "tir",
    "ons",
    "tor",
    "fre",
    "lor",
    "son"
]

def is_leap_year (year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False

def weekay_newyear(year):
    cycledWeekdays = cycle(weekdays)
    for i in range(1900, year + 1):
        if(is_leap_year(i-1)):
            next(cycledWeekdays)
        print(i, end=" ")

        print (next(cycledWeekdays))

weekay_newyear(1919)

def is_workday(day):
    if(day > 4):
        return False
    else:
        return True


def workdays(year):
    total_days = 261
    for i in range(1900, year + 1):

        if(is_leap_year(i-1) and is_workday(i)):
            return total_days + 1

        elif (is_leap_year(i-1) and is_workday(i) == False):
            return total_days - 1

        else:
            return total_days
   ## return total_days

def workdays_print(year):
    for i in range(1900, year + 1):
        print(i, workdays(year))
workdays_print(1919)