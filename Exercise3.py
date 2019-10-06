# Question 1
# a)
increaseNum = 3
while increaseNum <= 23:
    print(increaseNum)
    increaseNum += 4

# b)
decreaseNum = 30
while decreaseNum >= 20:
    print(decreaseNum)
    decreaseNum -= 2

# Question 2
# a)
for increNum in range(12, 25, 3):
    print(increNum)

# b)
for decreNum in range(46, 25, -4):
    print(decreNum)

# Question 3
count = 1
while count <= 3:
    print("{0}) Hellow UoW!".format(count))
    count += 1


# Question 4
for x in range(10, 0, -3):
    print("Countdown:" + str(x))
    print("Countdown:" + str(x - 1))
    print("Countdown:" + str(x - 2))

# Question 5
total = 0
numbers = 1
while numbers < 101:
    total += numbers
    numbers += 1
print(total)


# Question 6
for a in range(1, 11, 3):
    print("a = {0}".format(a))
    if a % 2 == 0:
        print("even")
    else:
        print("odd")

# Question 7
sumOfEvenNum = 0
i = 11
while i < 20:
    if i % 2 == 0:
        print("i = " + str(i))
        sumOfEvenNum += i
    i += 1
print("Total of even numbers is " + str(sumOfEvenNum))

# Question 8
sumOfOdd = 0
for odd in range(1, 100, 2):
    sumOfOdd += odd
print("Sum of odd numbers from 1 to 100 is " + str(sumOfOdd))

# Question 9
# a
column = 5
for row in range(1, column + 1):
    print("A|" * column)

# b
for row in range(1, 6):
    print("+=" * row)

# c
for row in range(5, 0, -1):
    print("B|" * row)

# d
for i in range(5, 0, -1):
    print(":>" * i, end="")
    print("  ", end="")
    print(":P" * (5 + 1 - i))

# e
for n in range(1, 9):
    if n % 3 != 0:
        print("{0})".format(n) * 5)
    else:
        print()

# Question 10
harmonicSum = 0
for i in range(1, 50001):
    harmonicSum += 1 / i
print(harmonicSum)

# Question 11
n = 20
fibo1 = 1
fibo2 = 1
fiboSum = fibo1 + fibo2
print("The first 20 Fibonacci numbers are: {0} {1}".format(fibo1, fibo2), end=" ")
for i in range(3, n + 1):
    fibo = fibo1 + fibo2
    fiboSum += fibo
    print(fibo, end=" ")
    fibo2 = fibo1
    fibo1 = fibo
print()
fibo_average = fiboSum / n
print("The average is {0}".format(fibo_average))

#  Question 12
while True:
    num = int(input("Enter a positive number: "))
    if num < 0:
        print("Please enter a positive number!")
    else:
        break
# Prime number is only divisible by 1 and itself

is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime == True:
    print("{0} is a prime number".format(num))
else:
    print("{0} is not a prime number".format(num))

# Question 13
userInput = int(input("User input length: "))
# a
print("Output pattern:")
for i in range(1, userInput + 1):
    if (i == 1) or (i == userInput):
        print("*" * 4)
    else:
        print("*  *")
# b
print("Output pattern:")
for i in range(1, userInput + 1):
    print(" " * (userInput + 1 - i), end="")
    print("*" * i)
# c
print("Output pattern:")
for i in range(userInput, 0, -1):
    print("*" * i)
# d
print("Output pattern:")
for row in range(0, userInput):
    for space in range((userInput - row) - 1):
        print(end=" ")
    for star in range(row + 1):
        print("*", end=" ")
    print()
# e
print("Output pattern:")
for row in range(userInput, 0, -1):
    for space in range((userInput - row) - 1):
        print(end=" ")
    for star in range(row, 0, -1):
        print("*", end=" ")
    print()
# f
# g

# PSLE Question
level = 250
triPerLevel = 1
totalTri = greyTri = whiteTri = 0

for tri in range(1, level + 1):
    if tri % 2 == 1:
        whiteTri += triPerLevel
    else:
        greyTri += triPerLevel

    triPerLevel += 2

totalTri = whiteTri + greyTri
print("total white: {0}".format(whiteTri))
print("total grey: {0}".format(greyTri))
print("Total triangles: {0}".format(totalTri))
grey_percent = round((greyTri / totalTri) * 100, 2)
print("Percentage of grey: {0}".format(grey_percent))
