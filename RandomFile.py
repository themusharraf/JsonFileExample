import random

#
# x = "WELCOME"
#
# print(random.choice(x))


# mylist = ["apple", "banana", "cherry"]
#
# print(random.choice(mylist))
#
"""
 randint(start, stop)
"""
# x = random.randint(3, 9)
#
# print(x)
# num = random.randint(1, 10)
# son = int(input("Enter a random number:"))
#
# if num == son:
#     print("ok")
# else:
#     print(f"no random number {num}")
#

"""
random game while
"""

while True:
    son = int(input("Enter a random number: "))
    num = random.randint(1, 10)
    if son == num:
        print("ok")
        break
    else:
        print(f"no random number -- > {num}")

print(f"dastur tugadi")
