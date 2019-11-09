# Question 1
def square(n):
    if n <= 1:
        return n
    else:
        return square(n - 1) + 2 * n - 1


# Question 2
def cube(n):
    if n == 1:
        return 1
    else:
        return cube(n - 1) + 3 * (square(n)) - 3 * n + 1


# Question 3
def mult(n, m):
    if m == 0:
        return
    else:
        return n + mult(n, m - 1)


# Question 4
def exp(n, m):
    if m == 0:
        return 1
    else:
        return mult(n, exp(n, m - 1))


# Question 5
def syracuse(n):
    print("{0}".format(n), end=" ")
    if n != 1:
        if n % 2 == 0:
            return syracuse(n // 2)
        else:
            return syracuse(3 * n + 1)


# Bonus Question
def check(n):
    if n == 0:
        return True
    if n == 1:
        return False

    return check(n - 2)


# Add up a list of numbers using recursive
def sum_list(num_list):
    if len(num_list) == 1:
        return num_list[0]

    return num_list[0] + sum_list(num_list[1:])


print(sum_list([1, 2, 3]))

