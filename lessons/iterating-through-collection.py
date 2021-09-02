"""example of looping through all characters in string"""

user_string: str = input("Give me a string! ")

# variable i is common counter variable name in program. i is short for iteratiion.
i: int = 0

while i < len(user_string):
    print(user_string[i])
    i = i + 1

print("Done!")
