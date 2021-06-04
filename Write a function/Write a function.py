def is_leap(year):
    if ( year >= 1900 and year <=100000):
        leap = False
        if ( (year % 4 == 0) and (year % 400 == 0 or year % 100 != 0) ):
            leap = True
        return leap

year = int(input())
print(is_leap(year))
