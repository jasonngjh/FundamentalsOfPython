# Question 1
header1 = "Student ID"
header2 = "Subject Code"
header3 = "Grade"
student1ID = "234D"
student1Subject = "CSIT110"
student1Grade = "A"
student2ID = "823E"
student2Subject = "CSIT100"
student2Grade = "B"
print("{0:<11}{1:<13}{2:^5}".format(header1, header2, header3))
print("{0:<11}{1:<13}{2:^5}".format(student1ID, student1Subject, student1Grade))
print("{0:<11}{1:<13}{2:^5}".format(student2ID, student2Subject, student2Grade))

# Question 2
age = int(input("Enter age: "))
VO2Max = int(input("Enter VO2Max: "))

if (age >= 12 and age <= 25 and VO2Max >= 40 and VO2Max <= 60) or (
    age >= 25 and age <= 35 and VO2Max >= 50 and VO2Max <= 70
):
    print("Allowed to participate in the match")
else:
    print("Not allowed to participate in the match")

# Question 3
num_of_even = 0

while True:
    user_input = input("Enter an integer or q to quit: ")
    if user_input == "q":
        break
    else:
        user_input = int(user_input)
        if user_input % 2 == 0:
            num_of_even += 1

print("You have entered {0} even integer(s).".format(num_of_even))

# Question 4
def print_inverted_triangle(height):
    for i in range(height, 0, -1):
        print(" " * (height - i), end="")
        print("*" * (2 * i - 1))


print_inverted_triangle(3)

# Question 5
# Refer to FinalRevision.docx
# 1: 4
# 2: 1
# 3: [7,8,8,9,3]
# 4: [7,8,8,3]
# 5: 2
# 6: [7,8,8,3]
# 7: [3,7,8,8]
# 8: [3,7,8,8]
# 9: [8,8,7,3]
# 10: 3
# 11: [8,2,8,7]

# Question 6
def multiply(n, m):
    r = 0
    if n > m:
        n, m = m, n
    for i in range(n):
        r += m
    return r


def exponent(n, m):
    result = 1
    for i in range(m):
        result = multiply(result, n)

    return result


print(exponent(3, 9))

# Question 7
def encrypt(word, alpha1, alpha2):
    wordToReturn = ""
    if len(alpha1) == len(alpha2):
        for letter in word:
            index = alpha1.index(letter)
            wordToReturn += alpha2[index]
        return wordToReturn
    else:
        return "Alpha1 and Alpha2 length are not the same"


alpha1 = "abcde"
alpha2 = "vwxyz"
print(encrypt("cab", alpha1, alpha2))

Question 8
def running_average(number_list):
    running_average = []
    average = 0
    count = 1
    for num in number_list:
        average = average * (count - 1) / count + num / count
        running_average.append(average)
        count += 1
    return running_average


number_list = [1, 2, 3, 4, 5]
print(running_average(number_list))

# Question 9
import random


def select_avatar(avarta_dict):
    names = list(avarta_dict.keys())
    name_index = random.randint(0, len(names) - 1)
    name = names[name_index]
    return name, avarta_dict[name]


power_list1 = ["earthquake", "fire ball"]
power_list2 = ["water spin", "sound blast", "thunder"]
power_list3 = ["wind", "tornado", " hurricane"]

avarta_dict = {"Seren": power_list1, "Isren": power_list2, "Elinu": power_list3}

avarta, power_list = select_avatar(avarta_dict)
print("Avarta {0}, has power {1}.".format(avarta, power_list))

# Question 10
def addNumber(num):
    if num != 0:
        r = num % 10
        return r + addNumber(num // 10)
    else:
        return 0


print(addNumber(12345))

# Question 11
def allSameLetter(string1, string2):
    if len(string1) != len(string2):
        return False

# # Lecturer Way
# buffer = []
# for letter in string2:
#     buffer.append(letter)

# allSameLetter = True
# for letter in string1:
#     if letter in buffer:
#         buffer.remove(letter)
#     else:  # letter not in buffer, stop here
#         allSameLetter = False
#         break
# return allSameLetter

#My way
    allSame = False
    for letter in string1:
        occurence_in_string1 = string1.count(letter)
        occurence_in_string2 = string2.count(letter)

        if occurence_in_string1 != occurence_in_string2:
            allSame = False
        else:
            allSame = True

    return allSame


print(allSameLetter("listen", "silent"))
print(allSameLetter("zoo", "soo"))
print(allSameLetter("zoos", "zoo"))

# Question 12
def min_and_max(number_list):
    lowest = number_list[0]
    highest = number_list[0]

    for i in range(1, len(number_list)):
        if lowest > number_list[i]:
            lowest = number_list[i]
        if highest < number_list[i]:
            highest = number_list[i]

    return lowest, highest


number_list = [2, 3, 6, 5, 4, 1, 3]

minimum, maximum = min_and_max(number_list)
print("Min: {0} Max: {1}".format(minimum, maximum))

