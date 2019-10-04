# Question 1
temperature = float(input("Enter temperature: "))
if temperature >= 100:
    print("Gas")
elif temperature > 0:
    print("Liquid")
else:
    print("Solid")

# Question 2
gender = input("Enter gender (m/f): ")
amount = float(input("Enter the amount: $"))

if amount >= 100:
    if (gender == "m") or (gender == "M"):
        print("Free gift: Shaver.")
    elif (gender == "f") or (gender == "F"):
        print("Free gift: Hand cream")
else:
    print("There is no free gift")

# Question 3
gender = input("Enter your gender (m/f): ")
age = int(input("Enter your age: "))

# compound condition (important in exam)
if ((gender == "m") or (gender == "M") and age >= 15) or (
    (gender == "f") or (gender == "F") and age >= 17
):
    print("You are allowed to participate")
else:
    print("You are not allowed to participate")

# Question 4
gender = input("Enter your gender (m/f): ")
age = int(input("Enter your age: "))

if age >= 12:
    if (gender == "m") or (gender == "M"):
        price = 20
    else:
        price = 12
else:
    if (gender == "m") or (gender == "M"):
        price = 12
    else:
        price = 10

print("The price is ${0}".format(price))

# Question 5
income = float(input("Enter your annual income: $"))
duration = int(input("Enter the duration of employement in current job : "))

if (income >= 30000) and (duration >= 2):
    print("Loan approved")
else:
    print("Loan not approved")

# Question 6
cost = float(input("Enter the total cost of purchase: $"))
bank = input("Enter the bank of your credit card (DBS, OCBC, etc.): ")

if cost >= 200:
    if bank == "DBS":
        cost *= 0.9
    elif bank == "OCBC":
        cost *= 0.85

cost = round(cost, 2)
print("Please pay ${0}".format(cost))

# Question 7
num = int(input("Enter a number: "))

if (num >= 5) and (num <= 10):
    print("Your number is {0}".format(num))
else:
    if num < 5:
        print("Number is less than 5")
    else:
        print("Number more than 10")
