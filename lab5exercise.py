# Question 1
def harmonic(n):
    if n == 1:
        return 1
    else:
        return harmonic(n - 1) + 1 / n


print(harmonic(5))

# Question 2
def fibo_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)


print(fibo_recursive(13))

# Question 3
def inverted_right_angle_triangle(n):
    if n != 0:
        print("*" * n)
        inverted_right_angle_triangle(n - 1)


print(inverted_right_angle_triangle(5))

# Question 4
def isEven(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return isEven(n - 2)


print(isEven(51))

# Question 5
def remainder(n, m):
    if m == n:
        return 0
    elif m > n:
        return n
    else:
        return remainder((n - m), m)


print(remainder(7, 2))

# Question 6
def isPrime(n, m):
    if n == 1 or m == n:
        return True
    elif n % m == 0:
        return False
    else:
        return isPrime(n, m + 1)


print(isPrime(50, 2))

Question 7
def largest(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        if num_list[0] < num_list[1]:
            del num_list[0]
        else:
            del num_list[1]
        return largest(num_list)


def largest(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        if num_list[0] < num_list[1]:
            new_num_list = num_list[1:]
            return largest(new_num_list)
        else:
            num_list[0], num_list[1] = num_list[1], num_list[0]
            new_num_list = num_list[1:]
            return largest(new_num_list)


print(largest([4, 7, 2, 8, 50, 10]))

