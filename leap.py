"""LEAP YEAR!
a year is identified as leap if it can be evenly divided by 4, unless
the year can be evenly divided by 100, it is NOT a leap
but also if evenly divided by 400, it is Leap"""

def is_leap(year):
    leap = False
    if year%4 == 0:
        # print (year%100)
        if year% 100 != 0:
            print year
            leap = True
        else:
            # print (year % 400)
            if year%400 == 0:
                leap = True
            else:
                leap = False
    else:
        leap = False
    return leap



year = int(raw_input())
print is_leap(year)