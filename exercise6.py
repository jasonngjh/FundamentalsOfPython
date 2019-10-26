# Question 1
name = "John Peter"
nameList = name.split(" ")

print(name)
print(len(name))
print(type(name))
print(len(nameList))
print(nameList[0])
print(nameList[1])
print(nameList[-1])
print(nameList[-2])

for namePart in nameList:
    print(namePart)

print((nameList[0].split("h"))[0])
# print(nameList[3])

# Question 2
nameList = ["Peter", "John"]

for i in range(len(nameList)):
    print(nameList[i])

for i in range(len(nameList) - 1, -1, -1):
    print(nameList[i])

# Question 4
names = ["alan", "peter", "john"]
# Write the code to add ‘mary’ to the end of list
names.append("mary")
print(names)

# Write the code to add ‘bob’ as the first item of the list
names.insert(0, "bob")
print(names)
# Write the code to remove ‘peter’ from the list
names.remove("peter")
print(names)

# Write the code to remove the 2nd item from the current list
del names[1]
print(names)

# Write the code to print out the number of people in the list.
print(len(names))

# Question 5
animals = "fish cat dog lion tiger mouse cow"
animals = animals.split(" ")
# a) Using a for loop, print all the words in the animals on separate lines.
for animal in animals:
    print(animal)
# b) Using a for loop, print all the 4 letter words in the animals on separate lines
for animal in animals:
    if len(animal) == 4:
        print(animal)

# Question 6
numberList = [14, 22, 28]
divisibleby7 = 0
for num in numberList:
    if num % 7 == 0:
        divisibleby7 += 1
print(divisibleby7)

# Question 7
num_list = list(range(0, 33, 4))
total = 0
for num in num_list:
    total += num
print("Sum: {0}".format(total))

# Question 8
num_list = list(range(0, 35, 3))
even_sum = 0
for num in num_list:
    if num % 2 == 0:
        even_sum += num
print("Even sum: {0}".format(even_sum))

# Question 9
even_counter = 0
for num in num_list:
    if num % 2 == 0:
        even_counter += 1
print("Even counter: {0}".format(even_counter))

# Question 10
def calculate_lucky_number(name):
    name_list = name.split(" ")
    fName = len(name_list[0])
    sName = len(name_list[1])
    tName = len(name_list[2])

    lucky_number = (2 * fName + sName) % 10 + tName
    return lucky_number


print(calculate_lucky_number("Tan Ah Kow"))

# Question 11
def calculateAverage(numberList):
    total = sum(numberList)
    return total / len(numberList)


print(calculateAverage([5, 10.20]))

# Question 12
def calculatePopulationStdDev(numberList):
    average = calculateAverage(numberList)
    sumOfDiffSq = 0
    for num in numberList:
        sumOfDiffSq += (average - num) ** 2
    population_std_dev = (sumOfDiffSq / len(numberList)) ** 0.5
    return population_std_dev


# Question 13
numberList = []
while True:
    userInput = int(input("Enter number: "))
    if userInput == -1:
        break
    else:
        numberList.append(userInput)

print(calculatePopulationStdDev(numberList))
