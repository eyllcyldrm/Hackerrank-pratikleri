# TASK
# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
#
# In the Gregorian calendar, three conditions are used to identify leap years:
#
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
#
# Artık Yıl Nasıl Hesaplanır
# Gregoryen takviminin kurallarına göre bir yılın artık yıl olup olmadığı şöyle belirlenir:
# 400'ün katı olan yıllar artık yıllardır.
#
# Bunun dışında 4'ün katı olan yıllar içerisinde yalnız 100'ün katı olmayan yıllar artık yıllardır.
# Task
#
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

def is_leap(year):
    leap = False
    if year >= 1900 and year <= pow(10, 5):
        if year % 400 == 0:
            leap = True

        elif year % 4 == 0 and year % 100 != 0:
            leap = True

        else:
            leap = False

    return leap


year = int(input())
print(is_leap(year))