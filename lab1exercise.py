# Question 1
print("{0:<11}{1:^11}{2}".format("Name", "Student ID", "Email"))
print("{0:<11}{1:^11}{2}".format("Jame Teo", "234D", "JaneTeo@csit110.org"))
print("{0:<11}{1:^11}{2}".format("Tan Ah Kow", "823E", "AhKowTan@csit110.org"))

# Question 2
print("{0:<14}{1:^9}{2}".format("Customer Name", "Card No.", "Mobile"))
print("{0:<14}{1:^9}{2}".format("Jame Teo", "S1234D", "+6596888442"))
print("{0:<14}{1:^9}{2}".format("Tan Ah Kow", "S6823E", "+6586321456"))

# Question 3
print("{0:<11}{1:<13}{2:^5}".format("Student ID", "Subject Code", "Grade"))
print("{0:<11}{1:<13}{2:^5}".format("234D", "CSIT110", "A"))
print("{0:<11}{1:<13}{2:^5}".format("823E", "CSIT100", "B"))

# Question 4
firstInt = int(input("Enter the first integer: "))
secondInt = int(input("Enter the second integer: "))
print(
    "The floor division of {0} by {1} is {2}.".format(
        firstInt, secondInt, (firstInt // secondInt)
    )
)
print(
    "The remainder of {0} divide by {1} is {2}.".format(
        firstInt, secondInt, (firstInt % secondInt)
    )
)

# Question 5
firstNum = float(input("Enter the first number: "))
secondNum = float(input("Enter the second number: "))

squareFirstNum = firstNum ** 2
sqrtSecondNum = secondNum ** (1 / 2)
print("The result is {0}".format(round(squareFirstNum + sqrtSecondNum, 2)))

# Question 6
firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))

a2 = firstNum ** 2
b2 = secondNum ** 2
c = (a2 + b2) ** (1 / 2)
print("The value of third number c is {0}".format(c))

# Question 7
gender = input("Enter gender (m/f):")
age = int(input("Enter age:"))

if (gender == "m" and age >= 15) or (gender == "f" and age >= 17):
    print("Allowed to participate in the contest")
else:
    print("Not allowed to participate in the contest")

# Question 8
age = int(input("Enter age:"))
vo2_max = int(input("Enter VO2 max:"))

if (age in range(18, 26)) and (vo2_max in range(30, 41)):
    print("Allowed to participate in the basketball match")
else:
    print("Not allowed to participate in the basketball match ")

# Question 9
gender = input("Enter gender:")
VO2Max = int(input("Enter VO2Max:"))

if (gender == "m" and VO2Max in range(40, 61)) or (
    gender == "f" and VO2Max in range(43, 61)
):
    print("Allowed to participate in the match")
else:
    print("Not allowed to participate in the match")
