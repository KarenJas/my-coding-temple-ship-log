'''1. The Range Riddle
import random
    #Task 1: Code Correction
for i in range(5,2,-1):
    print(i)
   
    #Task 2: Your Mood Today
mood = ["happy","sad","energetic","calm","nervouse","tired","excited"]
day =["monday","tuesday","wednessday","thursday","friday","saturday","sunday"]

for i in range(len(day)):
    todays_mood = random.choice(mood)
    print(f"{day[i]}: {todays_mood}")
    
    #Task 3: Going Backwards
for i in range(10,0,-1):
    print(i)


#2. Double Scoop with Nested Loops
    #Task 1: Code Correction
for i in range(3):
    for j in range(3):
        print("*", end="")
    print("\n",end="")
   
   #Task 2: Your Mood Tracker
mood = ["happy","sad","energetic","calm","nervouse","tired","excited"]
time_of_day = ["morning","afternoon","evening"]
day =["monday","tuesday","wednessday","thursday","friday","saturday","sunday"]
mood_tracker = []
for i in range(len(day)):
    current_day = day[i]
    print(f"{current_day}:")
    for j in range(len(time_of_day)):
        current_time = time_of_day[j]
        print(f"{current_time}- {random.choice(mood)}")
        
    #Task 3: Multiplication Table
for i in range(1,6):
    for j in range(1,6):
        product = i * j
        print(f"{i} x {j} = {product}  ",end="")
    print("\n",end="")

#3. Mastering Python's For Loop
    #Task 1: Code Correction
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

    #Task 2: Your Mood Swings
am_list = list(range(1,12))
am_list.insert (0,12)
pm_list = list(range(1,12))
pm_list.insert (0,12)
lunch_time = 1
am_time_mood = []
pm_time_mood = []
moods = ["Happy", "Sad", "Excited", "Relaxed", "Angry", "Surprised", "Content", "Stressed", "Confused", "Playful", "Grateful", "Inspired"]

for i in range(len(am_list)):
        am_time_mood_dic = { "TIME" : f"{am_list[i]} a.m.","MOOD": random.choice(moods) }
        am_time_mood.append(am_time_mood_dic)
print(am_time_mood)

for i in range(len(pm_list)):
        if pm_list[i] == lunch_time:
                continue
        pm_time_mood_dic = { "TIME" : f"{am_list[i]} p.m.","MOOD": random.choice(moods) }
        pm_time_mood.append(pm_time_mood_dic)
print(pm_time_mood)

    #Task 3: The Persistent Loop
number_list = list(range(1,11))
chosen_number = 1
for num in range(len(number_list)):
    if num == chosen_number:
        print("found number")
        break     
else:
    print("number not found")

#4. The Marshmallow Increment Challenge
    #Task 1: Increment at the Start
#I predict that it will output the print statement 5 times
marshmallows = 0
while marshmallows < 5:
    marshmallows += 1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
#First the program will check to see if the value of marshmallows is less than 0
#If it is true the program will then add 1 to the value of marshmallows and then print the statment
#Once the value of marshmallows reaches the number 6 the loop will no longer be true and will stop

    #Task 2: Increment at the End
#I predict that the output will remain the same as the previous code
marshmallows = 0
while marshmallows < 5:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows += 1
#In this output the print statment number starts at 0 and ends at 4 istead or starting at 1 and ending on 5
#This is caused becasue the print stament uses the marshmallow variable before it is updated to the correct number making it be one off
    
    #Task 3: Off-by-One Error Investigation
marshmallows = 0
#code with one off error 
while marshmallows < 11:
    marshmallows +=1
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
#fixed code
#increasing the marshmallow count after the print statment allows it to be delayed by one as to not exceed the 10 marshmallow limit regardless of the loop condition
#another way to correct the code would be to set the loop condition to less than 10 and flip the order of the loop
#it is import to prioritize the order in which you increment because it can cause a one off error
while marshmallows < 11:
    print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
    marshmallows +=1


#5. Loop Condition Logic
    #Task 1: Loop Condition Exploration
number = 0
# Because the loop condition is set to always be true the loop will never end
# Thanks to the break statment once the number variable reaches 6 the loop will instantly stop
while True:
    number += 1
    if number == 6:
        break
    print(number)

    #Task 2: Conditional Exit
# The loop will first check the value of the number variable 
# as long as the number variable is lesss than 5 the loop will increas the number variable by 1
# Once the number variable reaches 5 the loop will end 
while number < 5:
    number += 1
    print(number)

    #Task 3: Loop with Multiple Conditions
#Combining conditions allows us to be more spesific about when a loop is executated making it more complex than a loop with a singular condition
list = [1,2,3,4,5,]
end = 0
while 1 and 2 in list:
    end += 1
    print(end)
    if end == 5:
        break

#6. The Art of Loop Control
    #Task 1: Using else with while
fruits = ["apple", "banana", "orange", "grape", "watermelon", "kiwi", "strawberry", "mango", "pineapple", "pear"]
# The loop will first check to see if the condition is true 
# If the condition is false the else clause will run
while "apple" in fruits:
    if "apple" in fruits:
        print("Found appple")
        break
else:
    print("Apple not found in list")

    #Task 2: Loop Interruption with break
time_of_day = 12
# The code will output the time of day in order but once it reaches 3 pm the if stamement condition will be true and break the loop 
while True:
    if time_of_day == 12 :
        print(str(time_of_day),"am")
        time_of_day = 0
        while True:
            if time_of_day < 11:
                time_of_day += 1
                print(str(time_of_day),"am")
                if time_of_day == 11:
                    time_of_day = 12
                    while True:
                        if time_of_day == 12 :
                            print(str(time_of_day),"pm")
                            time_of_day = 0
                            while True:
                                if time_of_day < 11:
                                    time_of_day += 1
                                    if time_of_day == 3:
                                     break
                                    print(str(time_of_day),"pm")
    

    #Task 3: Skipping Iterations with continue
#the continue statment allows the code to skip over multiples of 3 
task3_numbers = list(range(1,31))
index = 0
new_task3_numbers = []
while index < 30: 
    if task3_numbers[index] % 3 == 0 :
        index += 1
        continue
    new_task3_numbers.append(task3_numbers[index])
    index +=1
print(new_task3_numbers)

    #Task 4: The Placeholder pass
#the loop uses pass to allow the code to run and add code later on 
# Pass might be useful when you need to run the code but dont have it finished yet
number_check = [list(range(1,10))]
while True:
    if 5 in number_check:
        pass


#7. Python's Random Game Night
    #Task 1: Dice Rolling Simulator

# Initialize a dictionary to keep track of dice roll frequencies
roll_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Let's roll the dice 10 times
for _ in range(10):
    dice_roll = random.randint(1, 6)
    # Update the roll_count dictionary
    roll_count[dice_roll] += 1
    print("You rolled a " + str(dice_roll) + "!")

# Print out the frequency of each number
for number, frequency in roll_count.items():
    print(f"Number {number} was rolled {frequency} times.")

    #Task 2: Random Choice Game
user_guess = int(input("Guess: "))
dice = [1,2,3,4,5,6]
random_roll = random.choice(dice)

if user_guess == random_roll :
    print( "You are correct! :)")
else:
    print("You are Wrong :(")

    #Task 3: Shuffling a Deck
#random.shuffle() can be used to randomize an action and allow the user to play with it 
#by having them guess the output or allowing them to use it as a tool like in the dice rolling game above
import random
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
print(deck)
random.shuffle(deck)
print(deck)
'''