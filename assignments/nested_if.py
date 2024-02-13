# 1. Nested Decisions: The Adventure Game 
    # Task 1 
'''
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    # Task 3 
    else:
        pass
elif place == "cave":
    print("You find a hidden treasure!")
    # Task 2
    action = input("Do you want to light a torch or proceed in the dark?: ")
    if action == "light a torch":
        print("You find writting on walls")
    elif action == "proceed in the dark":
        print("Yoou stumble into a trap!")
    # task 3 
    else: 
        pass
else:
    pass


# 2. Quick Decisions: The Event Planner 
    # Task 1 
attendees = int(input("Enter number of attendees: "))
    #Task 3
food = input("would you like to serve vegetarian food (yes/no)?: ")
    #Task 1
if attendees > 100 :
    print("large hall")
        # Task 2
    print("You should obtain additional facilities like an audio system or projector")
else: 
    print("conference room")

    # Task 3
if food == "yes":
    print("We recoment Veggie Delight Caters")
elif food == "no":
    print("We recoment Gourmet Meals Caterers")

'''
# 3. Silent Failures: The Error Handler 
    # Task 1 
try:
    x = 1 / 0
except ZeroDivisionError:
    pass
    # Task 2 
try:
    y = 1 / "1"
except TypeError:
    pass
try:
    x = 4
    if x > 5:
        print("x is greater than 5")
except SyntaxError:
    pass

# Task 3 
file_name = input("Enter filename: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    pass
