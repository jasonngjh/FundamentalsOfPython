# # Quesition 1
# def even_index_string(str):
#     string = ""
#     for i in range(0, len(str)):
#         if i % 2 == 0:
#             string += str[i]
#     return string


# print(even_index_string("abcdef"))

# # Question 2
# def upper_half_string(str):
#     string = ""
#     if len(str) % 2 == 0:
#         string = str[0 : (len(str) // 2)]
#     else:
#         string = str[0 : (len(str) // 2) + 1]
#     return string


# print(upper_half_string("abcdefg"))

# # Question 3
# def middle_char_in_string(str):
#     char = ""
#     if len(str) % 2 == 1:
#         char = str[len(str) // 2]
#     else:
#         char = str[len(str) // 2 - 1] + str[len(str) // 2]
#     return char


# print(middle_char_in_string("abcdef"))

# # Question 4
# def fact(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     return fact


# print(fact(4))

# # Question 5
# def multiply(num1, num2):
#     number = 0

#     if num1 > num2:
#         num1, num2 = num2, num1

#     for i in range(num1):
#         number += num2

#     return number


# print(multiply(6000, 5))

# # Question 6
# def power(num1, num2):
#     value = 1
#     for i in range(num2):
#         value = multiply(value, num1)

#     return value


# print(power(5, 3))

# # Question 7
# import random


# def number_guessing_game():
#     secret_number = random.randint(1, 100)
#     print("I have chosen a secret number between 0 and 100.")
#     while True:
#         num = int(input("Enter a guess: "))
#         if num > secret_number:
#             print("Lower than that")
#         elif num < secret_number:
#             print("Higher than that")
#         else:
#             print("Hooray! You are correct!")
#             break


# number_guessing_game()

# # Question 8
# found = False
# for n in range(3, 6):
#     for x in range(1, 101):
#         for y in range(1, 101):
#             for z in range(1, 101):
#                 x_term = x ** n
#                 y_term = y ** n
#                 z_term = z ** n
#                 if x_term + y_term == z_term:
#                     found = True
# if found:
#     print("Found a solution")
# else:
#     print("No solution")

# Question 9
alphabet = "abcdefghijklmnopqrstuvwxyz"


def get_char_index(c):
    char_index = -1
    for i in range(len(alphabet)):
        if alphabet[i] == c:
            char_index = i
            break

    return char_index


def encrypt_usingCaesar(text, key):
    cipher_text = ""
    for char in text:
        char_index = get_char_index(char)
        cipher_index = (char_index + key) % len(alphabet)
        cipher_text += alphabet[cipher_index]

    return cipher_text


encryptedtext = encrypt_usingCaesar("yomama", 5)
print(encryptedtext)

# Question 10
def decrypt_usingCaesar(text, key):
    clear_text = ""
    for char in text:
        char_index = get_char_index(char)
        cipher_index = (char_index - key) % len(alphabet)
        clear_text += alphabet[cipher_index]

    return clear_text


decryptedtext = decrypt_usingCaesar(encryptedtext, 5)
print(decryptedtext)
