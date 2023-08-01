# f-strings output the value assigned to the stated variable
# gives a clean look for any inputted code from the user.
# youtuber = "YR"
# print(f"subscribe to {youtuber}") 
adjective = input("Your adjective ")
noun = input("Your noun ")
place = input("Your place ")
item = input("Your item ")
food = input("Your choice of food ")

# the \ makes a new line possible from these long strings.
madlib = f"Chinese New Year is so {adjective}. You get to gather with {noun}, \
go to {place} and get some {item} and eat some {food} during this festive season."

print(madlib)
