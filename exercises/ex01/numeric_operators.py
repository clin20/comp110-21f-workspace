"""User inputs 2 numbers and 4 operators are used."""

__author__: str = "730508262"

first_num: int = int((input("Left-hand side: ")))
second_num: int = int((input("Right-hand side: ")))

print(str(first_num) + " ** " + str(second_num) + " is " + str((first_num) ** (second_num)))

print(str(first_num) + " / " + str(second_num) + " is " + str(first_num / second_num))


print(str(first_num) + " // " + str(second_num) + " is " + str(first_num // second_num))


print(str(first_num) + " % " + str(second_num) + " is " + str(first_num % second_num))