# 1
degree = int(input("Enter temperature in degree celsius: "))
kelvin = degree + 273.15
print("{0} C is {1} K".format(degree, kelvin))

# 2
degree = int(input("Enter temperature in degree celsius: "))
fahrenheit = round((degree * 9 / 5) + 32, 2)
print("{0} C is {1} F".format(degree, fahrenheit))

# 3
name1 = "John"
score1 = 56
name2 = "Mary"
score2 = 65
name3 = "Peter"
score3 = 89

print("{0:<10}{1:<5}".format("Name", "Score"))
print("{0:<10}{1:<5}".format(name1, score1))
print("{0:<10}{1:<5}".format(name2, score2))
print("{0:<10}{1:<5}".format(name3, score3))

# 4
power = int(input("Enter power: "))
power_header = "Power of {0} is".format(power)
print()
print("{0:<6} {1:<12}".format(1, 1 ** power))
print("{0:<6} {1:<12}".format(2, 2 ** power))
print("{0:<6} {1:<12}".format(3, 3 ** power))

# 5
from datetime import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

today = datetime.now()
todayYear = today.year

diff = 100 - age
years_to_100 = today.year + diff
print("{0}, in year {1}, you will be 100 years old".format(name, years_to_100))

