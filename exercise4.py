# Question 1
def subtract_two_numbers(n1, n2):
    r = n1 - n2
    return r


r = subtract_two_numbers(10, 5)
print(r)

# Question 2
def multiply_two_numbers(n1, n2):
    r = n1 * n2
    return r


r = multiply_two_numbers(10, 5)
print(r)

# Question 3
def handlebars(s1, s2):
    print("--" + str(s1) + "--" + str(s2) + "--")


handlebars("me", "you")

# Question 4
def area_circle(radius):
    return 3.142 * (radius ** 2)


def area_triangle(base, height):
    return 0.5 * base * height


shaded_region = round(
    (area_triangle(10, 5) - area_triangle(3, 2)) + (area_circle(6) * 2), 3
)

print("Total area of the shaded region is {0}".format(shaded_region))

# Question 5
def cal_discount(price, discount):
    return price * (discount / 100)


price = float(input("Enter the original price of the item:- "))
discount = float(input("Enter the discount in percentage:- "))

discount_amount = round(cal_discount(price, discount), 2)

print("You get to save ${0}".format(discount_amount))

# Question 6
def getPrice(gender, age):
    if age >= 12:
        if gender == "male":
            return 20
        else:
            return 18
    else:
        if gender == "male":
            return 12
        else:
            return 10


print(getPrice("male", 10))
print(getPrice("female", 15))

totalcost = getPrice("male", 42)
totalcost += getPrice("female", 42)
totalcost += getPrice("male", 11)
totalcost += getPrice("male", 10)

print("Total cost of family is ${0}".format(totalcost))

# Question 7
def number_range(n1, n2, n3, n4):
    small = n1
    if n2 < small:
        small = n2
    if n3 < small:
        small = n3
    if n4 < small:
        small = n4

    large = n1
    if n2 > large:
        large = n2
    if n3 > large:
        large = n3
    if n4 > large:
        large = n4

    return small, large


min_num, max_num = number_range(3, 2, 7, 5)
print("Min: {0} Max: {1}".format(min_num, max_num))

# Question 8
import random


def biased_dice():
    r = random.randint(1, 100)
    if r <= 10:
        num = 1
    elif r <= 30:
        num = 2
    elif r <= 50:
        num = 3
    elif r <= 80:
        num = 4
    elif r <= 95:
        num = 5
    else:
        num = 6

    return num


for i in range(1, 7):
    print(str(biased_dice()))

# Question 9
def is_prime(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime


def printPrime(a, b):
    for i in range(a, b + 1):
        if is_prime(i):
            print("{0}".format(i), end=" ")


printPrime(10, 1000)

# Question 10
def hexagonal_number(n):
    for i in range(1, n + 1):
        hex_num = 2 * (i ** 2) - i
        print("{0}".format(hex_num), end=" ")


hexagonal_number(10)


def is_hexagonal_number(num):
    is_hex_num = True
    n = 1
    while True:
        hex_num = 2 * (n ** 2) - n
        if hex_num == num:
            is_hex_num = True
            break
        if hex_num > num:
            is_hex_num = False
            break
        n += 1
    return is_hex_num


print(is_hexagonal_number(15))
print(is_hexagonal_number(30))
