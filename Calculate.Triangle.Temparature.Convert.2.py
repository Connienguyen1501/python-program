# Functions:

# Code 1:

def triangle_area(base, height):
    area = (1.0 /2) * base * height
    return area

#Test code 1:
a1 = triangle_area(16,8)
print a1

a2 = triangle_area(2,4)
print a2

#Code 2:
def fahrenheitit2celcius(fahrenheit):
    celcius = 5.0/9.0 * (fahrenheit) - 32
    return celcius

#Test Code 2:
c1 = fahrenheitit2celcius(45)
print c1

c2 = fahrenheitit2celcius(85)
print c2

#Code 3:
def celciusit2fahrenheit(celcius):
    fahrenheit = 9.0/5.0 * (celcius) + 32
    return fahrenheit

#Test Code 2:
f1 = celciusit2fahrenheit(32)
print f1

f2 = celciusit2fahrenheit(-2)
print f2

#Code 4:
def fahrenheitit2celcius(fahrenheit):
    celcius = 5.0/9.0 * (fahrenheit) - 32
    kevin = celcius + 273.15
    return kevin

#Test Code 4:
k1 = fahrenheitit2celcius(78)
print k1

k2 = fahrenheitit2celcius(-78)
print k2

#Code 5:
def square_area(base,height):
    area = (base + height) *2
    return area

#Test Code 5:
s1 = square_area(10,4)
print s1

