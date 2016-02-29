# Check if a year is leap year or not

def is_a_leap_year(year):
    if (year % 400) == 0 :
        return True
    elif (year % 100) == 0 :
        return True
    elif (year % 4) == 0:
        return True
    else:
        return False
    
year = 2006
leap_year = is_a_leap_year(year)

if leap_year:
    print year, "is a leap year"
else:
    print year, "is not a leap year"
    
year = 2078
leap_year = is_a_leap_year(year)

if leap_year:
    print year, "is a leap year"
else:
    print year, "is not a leap year"
    
year = 2016
leap_year = is_a_leap_year(year)

if leap_year:
    print year, "is a leap year"
else:
    print year, "is nto a leap year"