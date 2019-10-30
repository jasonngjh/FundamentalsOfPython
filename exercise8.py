# Question 1
marks = {"John": [76, 65, 43], "Mary": [68, 56, 74], "Peter": [46, 55, 48]}

# Question 2
marks["Ada"] = [56, 45, 65]

# Question 3
marks["Mary"][2] = 87

# Question 4
del marks["Peter"]
print(marks)

# Question 6
def showMarks(marks, name):
    print("Marks for " + name)
    print("Science:" + str(marks[name][2]))
    print("Math:" + str(marks[name][1]))
    print("English:" + str(marks[name][0]))
    print()


showMarks(marks, "John")

# Question 7
def showAllMarks(marks):
    print("Show all students marks")
    for name in marks:
        showMarks(marks, name)


showAllMarks(marks)

# Question 8
for name in marks.keys():
    score = marks.get(name)[0]
    if score >= 50:
        print(name)

# Question 9

Laptops = {"acer": 20, "hp": 10, "toshiba": 15, "apple": 12}

# a)
for brand in Laptops.keys():
    print("{0}:{1}".format(brand, Laptops.get(laptop)))

# b)
for laptop in Laptops.keys():
    if Laptops.get(laptop) >= 15:
        print(laptop)

# c)
values = Laptops.values()
total = 0
for num in values:
    total += num

print(total)

# Question 10

names = ["alan", "peter", "mary", "john"]
ages = [17, 18, 19, 20]

person = {}
for i in range(len(names)):
    key = names[i]
    value = ages[i]
    person[key] = value

print(person)

# Question 11
users = {
    "matt": {"phone": "1234", "email": "ma77@code.org"},
    "joe": {"phone": "9823", "email": "mjoe@python.com"},
    "lee": {"phone": "3463", "email": "lee01@gmail.com"},
}


def view():
    print("View User(s)")
    userInput = int(input("Enter your input (1: View All,  2:View One users): "))
    if userInput == 1:
        for user in users:
            print("User: " + user)
            print("Phone: " + users[user]["phone"])
            print("Email: " + users[user]["email"])
    elif userInput == 2:
        userName = input("Enter user name: ")
        info = users.get(userName)
        if info is None:
            print("User not found")
        else:
            print("User: " + userName)
            print("Phone: " + users[userName]["phone"])
            print("Email: " + users[userName]["email"])
    else:
        print("Invalid input")


def add():
    print("Adding new user")
    userName = input("Enter the new name: ")
    info = users.get(userName)
    if info is None:
        phone = input("Enter new phone: ")
        email = input("Enter new email: ")

        info = {"phone": phone, "email": email}
        users[userName] = info
        print("{0} is added! ".format(userName))
    else:
        print("User is found!")


def update():
    print("Update user")
    userInput = input("Enter user to update: ")
    info = users.get(userInput)
    if info is None:
        print("User not found")
    else:
        option = int(input("Enter which to update (1:Phone, 2: Email)"))

        if option == 1:
            phone = input("Enter new phone: ")
            (users[userInput])["phone"] = phone
        elif option == 2:
            email = input("Enter new email: ")
            (users[userInput])["phone"] = email
        else:
            print("Invalid option")

        print("{0} is updated! ".format(userInput))


def delete():
    print("Deleting user")
    userInput = input("Enter user to update: ")
    info = users.get(userInput)
    if info is None:
        print("User not found")
    else:
        del users[userInput]
        print("{0} is deleted!".format(userInput))


def main():
    options = {1: view, 2: add, 3: update, 4: delete}
    while True:
        userInput = int(
            input("Enter your input (1: View, 2: Add, 3: Update, 4: Delete 5: Exit):  ")
        )

        if userInput == 5:
            break
        if userInput > 5 or userInput < 1:
            print("Invalid input")
        else:
            options[userInput]()


main()
