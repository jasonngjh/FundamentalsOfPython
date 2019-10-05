# Question 1
# a)
"""
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
for odd in range(1, 100,2):
    sumOfOdd += odd
print("Sum of odd numbers from 1 to 100 is " + str(sumOfOdd))

# Question 9
# a
for n in range(1, 6):
    print("A|A|A|A|A|")
"""
# b
for n in range(1, 6):
    print("+=")
