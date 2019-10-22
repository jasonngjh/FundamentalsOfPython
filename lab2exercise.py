# Question 1
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

print("The Times table by 5 from {0} to {1}".format(first, second))
for i in range(first, second + 1):
    print("5 x {0} = {1}".format(i, (5 * i)))

# Question 2
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

print("The summation table from {0} to {1}".format(first, second))
for i in range(first, second):
    print("{0} + {1} = {2}".format(i, i + 1, (i + (i + 1))))

# Question 3
no_of_odd = 0
while True:
    usr_input = input("Enter an integer or q to quit: ")
    if usr_input != "q":
        if (int(usr_input) % 2) == 1:
            no_of_odd += 1
    else:
        break
print("You have entered {0} odd integer(s).".format(no_of_odd))

# Question 4
no_of_even = 0
while True:
    usr_input = input("Enter an integer or q to quit: ")
    if usr_input != "q":
        if (int(usr_input) % 2) == 0:
            no_of_even += 1
    else:
        break

print("You have entered {0} even integer(s).".format(no_of_even))

# Question 5
no_of_vowels = 0
vowels = ["a", "e", "i", "o", "u"]
while True:
    usr_input = input("Enter a letter or - to quit: ")
    if usr_input != "-":
        if usr_input in vowels:
            no_of_vowels += 1
    else:
        break
print("You have entered {0} vowel(s).".format(no_of_vowels))

# Question 6
def print_tree(height):
    if height == 1:
        print("*")
    else:
        for i in range(1, height + 1):
            print(" " * (height - i), end="")
            print("*" * (i * 2 - 1))


print_tree(3)

# Question 7
def print_tree(height):
    if height == 1:
        print("*")
    else:
        for i in range(1, height + 1):
            if i == 1 or i == height:
                print(" " * (height - i), end="")
                print("*" * (i * 2 - 1))
            else:
                print(
                    "{0}{1}{2}{3}".format(
                        " " * (height - i), "*", " " * (i * 2 - 3), "*"
                    )
                )


print_tree(5)

# Question 8
def print_inverted_triangle(height):
    if height == 1:
        print("*")
    else:
        for i in range(height, 0, -1):
            print(" " * (height - i), end="")
            print("*" * (i * 2 - 1))


print_inverted_triangle(3)

# Question 9
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

# 1st way
num1, num2 = num2, num1
# 2nd way
tempNum = num1
num1 = num2
num2 = tempNum

print("After swap:")
print(num1)
print(num2)

# Question 10
import random


def three_sided_dice():
    num = random.randint(1, 3)
    if num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"


for i in range(1, 10):
    print(three_sided_dice())
