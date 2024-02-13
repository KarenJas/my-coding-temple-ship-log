# 1. Movie Night Decision 
mood = input("What mood are you in?: ")
weather = input("What is todays weather like?: ")

if mood == "happy" and weather == "sunny":
    print("You could watch a comedy!")
elif mood == "happy" and weather !=  "sunny":
    print("You watch a a romance!")
elif mood == "sad":
    print("you should watch a drama!")
else:
    print("You should watch an adventure movie!")


# 3. STudent Discount Eligibility
grade = input("What is your grade?: ")
sports_team = input("Are you part of a sports team (yes/no)?: ")
drama_club = input("Are you part of the drama club (yes/no)? : ")

if grade == "A":
    if sports_team == "yes":
        print("You will get a 20% discount")
    else :
        print("You will get a 10% discount")
elif grade == "B" and drama_club == "yes":
    print("You will get a 15% discount")
    
