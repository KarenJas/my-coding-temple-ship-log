# Exercise 1: Traffic Light Simulator 
light_color = input("Enter the traffic light color: ")

# making if else statement to determin what to do based on the light color
if light_color == "green" :
    print("You may drive foward")
elif light_color == "yellow" :
    print("You should slow down before the light turns red")
else :
    print("stop before the light")

# Exercise 2: Movie Age Restrictions
print("Lets see if you can watch the movie")
age = int(input("How old are you?: "))
rating = input("What is the rating of the movie?: ")

# if statement to determin what rated movie you are allowed to watch


 
if rating == "G":
    print("You can watch it!")
elif rating == "PG" and age >= 7:
    print("You can go for it!")
elif rating == "PG-13" and age >= 13 :
    print("You can go for it!")
elif rating == "R" and age >= 17 : 
    print("You can go for it!")
else:
    print("Aww you cant watch it")