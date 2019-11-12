# Question 1
# 1: 4
# 2: 3
# 3: [3,4,4,5,3]
# 4: [3,4,5,3]
# 5: 2
# 6: [3,4,5,3]
# 7: [3,3,4,5]
# 8: [3,3,4,5]
# 9: [5,4,3,3]
# 10: 3
# 11: [5,2,4,3]

# Question 2
results = {
    "S134": {"name": "Jane", "grade": "D"},
    "S456": {"name": "John", "grade": "C"},
    "S654": {"name": "Peter", "grade": "HD"},
}

studentid = input("Enter a student id: ")
if studentid in results:
    studentresult = results.get(studentid)
    print(
        "Student result found: Name: {0}, Grade: {1}".format(
            studentresult["name"], studentresult["grade"]
        )
    )
else:
    print("Student id not found")

# Question 3
import random


def lucky_customer(customer_shopping_dict):
    # customer, shopping_list = random.choice(list(customer_shopping_dict.items()))
    n = random.randint(0, len(customer_shopping_dict))
    keys = list(customer_shopping_dict)
    customer = keys[n]
    shopping_list = customer_shopping_dict.get(customer)
    return customer, shopping_list


shopping_list1 = ["cake", "apple pie"]
shopping_list2 = ["salad", "pasta", "potato"]
shopping_list3 = ["orange", "apple", "soft drink"]

customer_shopping_dict = {
    "John": shopping_list1,
    "Peter": shopping_list2,
    "Mary": shopping_list3,
}

name, shopping_list = lucky_customer(customer_shopping_dict)
print("Congratulations {0}, you shopping list {1} is free!".format(name, shopping_list))
