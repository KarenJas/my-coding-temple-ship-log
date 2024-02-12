# Exercise 1: Traffic Light Simulator 
light_color = input("Enter the traffic light color: ")

# making if else statment to determin what to do based on the light color
if light_color== "green" or "Green":
    print("You may drive foward")
elif light_color== "yellow" or "Yellow":
    print("You should slow down before the light turns red")
else :
    print("stop before the light")

