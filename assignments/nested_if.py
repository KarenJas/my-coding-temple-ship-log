'''
# 1. Nested Decisions: The Adventure Game 
    # Task 1 
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
   
    # Taskt 1
print("large hall") if attendees >= 100 else print("confrence room")
   
    # Task 2
print("We recomend adding an audio system") if attendees >= 100 else print("We recomend adding a projector")
    
    # Task 3
print("We recomend Veggie Delight Caters") if food == "yes" else print("We recoment Gourmet Meals Caterers")



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
    with open(file_name) as file:
        content = file.read()
        print("File content: ", content)
except FileNotFoundError:
    pass


# 4. Nested Quick Decisions: The Shopping Assistant 
    # Task 1
weather = input("Enter the weather: sunny, rainy, cold, windy, snowy: ")
clothing = "sunglasses" if weather == "sunny" else "umbrella" if weather == "rainy" else "sweater" if weather == "cold" else "hat" if weather == "windy" else "boots" # Task 2 
    # Task 3
accessory = "sunscreen" if weather == "sunny" else "waterprooof jacket" if weather == "rainy" else "scarf" if weather == "cold" else "windbreaker" if weather == "windy" else "gloves"
print(clothing)
print(accessory)
'''

# 5. The Silent Logger: System Monitor 
    # Task 1 
import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_space = random.randint(0, 100)
if cpu_usage > 90:
        print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
        pass

if memory_usage > 90:
        print("High memory usage!")
elif memory_usage > 80 and memory_usage <= 90:
        pass

if disk_space > 90:
        print("Low disk space!")
elif disk_space > 80 and disk_space <= 90:
        pass

