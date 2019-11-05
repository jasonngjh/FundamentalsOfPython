# Question 1
def harmonic(n):
    if n == 1:
        return 1
    else:
        sum = 1
        for denominator in range(2, n + 1):
            sum += 1 / denominator
        return sum


print(harmonic(2))

# Question 2
def is_prime(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    return is_prime


def prime(n):
    counter = 0
    running_num = 2
    while True:
        if is_prime(running_num):
            counter += 1
        if counter == n:
            break
        running_num += 1

    return running_num


print(prime(6))

# Question 3
def sum_of_digit(num):
    num_string = str(num)
    sum = 0
    for digit in num_string:
        print(digit)
        sum += int(digit)
    return sum


print(str(sum_of_digit(32768)))

# Question 4
import string

alphabet = string.ascii_lowercase


def triangle_num(count):
    t = (count * (count + 1)) / 2
    return int(t)


def is_triangle_word(word):
    word_value = 0
    for letter in word.lower():
        word_value += alphabet.index(letter) + 1

    counter = 1
    while triangle_num(counter) <= word_value:
        if triangle_num(counter) == word_value:
            return True
        counter += 1

    return False


print(is_triangle_word("SKY"))

# Question 5
import random


def biased_dice():
    r = random.randint(1, 100)
    if r <= 25:
        num = 1
    elif r <= 40:
        num = 2
    elif r <= 45:
        num = 3
    elif r <= 60:
        num = 4
    elif r <= 70:
        num = 5
    else:
        num = 6
    return num


freq_counter = [0, 0, 0, 0, 0, 0]
for i in range(10000):
    num = biased_dice()
    freq_counter[num - 1] += 1

for i in range(len(freq_counter)):
    percent = freq_counter[i] / 10000 * 100
    print("{0} : {1}%".format(i + 1, percent))
