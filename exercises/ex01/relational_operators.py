"""User inputs collected and then 4 relational operators used."""

__author__: str = "730508262"

first_num: int = int((input("Left-hand side: ")))
second_num: int = int((input("Right-hand side: ")))

print(str(first_num) + " < " + str(second_num) + " is " + str((first_num) < (second_num)))

print(str(first_num) + " >= " + str(second_num) + " is " + str(first_num >= second_num))


print(str(first_num) + " == " + str(second_num) + " is " + str(first_num == second_num))


print(str(first_num) + " != " + str(second_num) + " is " + str(first_num != second_num))