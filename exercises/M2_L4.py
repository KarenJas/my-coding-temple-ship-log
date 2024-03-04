# utilize for loops to iterate over multiple lists and organize event details without using functions 
'''
event_names = ["Event1", "Event2", "Event3"]
event_dates = ["2024-03-01", "2024-03-15", "2024-04-01"]
event_locations = ["Location1", "Location2", "Location3"]
event_organized = [ ]
for i in range(len(event_dates)):
    event_dic = {
        "event" : event_names[i],
        "date" : event_dates[i],
        "location" : event_locations[i]
    }
    event_organized.append(event_dic)
print (event_organized)

# use for loops with rage function to assign seats in a classroom setting 
kids = ["Kid1","kid2","kid3","Kid4","kid5","kid6","kid7","kid8"]
table1 = []
table2 = []

for i in range(len(kids)):
    if i % 2 == 0:
        table1.append(kids[i])
    else:
        table2.append(kids[i])

print(table1)
print(table2)
'''
'''need to redo this and assign each kid their individual seat'''
# 30 kids - 5 rows - 7 in each row 



# while loops 
'''
time = 13

while time > 0:
    time -= 1
    print( time )
# break
temperature = 70
battery_life = 5
full_charge_time_hours = 2

while battery_life > 0 :
    if full_charge_time_hours < 2 :
        if temperature < 80 :
            print ("battery is ok")
            battery_life -= 1
        else :
            print (" charger works but temperature too high")
            battery_life -= 1
    if full_charge_time_hours > 1 :
        if temperature < 80:
            print( "might need new charger but temperature is fine")
            battery_life -= 1
        else:
            print( "need new battery")
            battery_life-= 1
# break
coffe_type = [1,2,3,4,5,6,7,8,9,10]
people_in_store = 10
while len(coffe_type) > 0 :
    question = input("would u like coffe: ")

    if question == "yes" :
        coffe_type.pop()
        print("here you are. Have a nice day")
    elif question == "no":
        print ("ok have a nice day")
# break
floors = [1,2,3]    
floor_rooms1 = ["q","w","e"]
floor_rooms2 = ["a","s","d"]
floor_rooms3 = ["z","x","c"]
people_in_elevator = 3
while people_in_elevator > 0 :
    question = input("what room are you looking for? : ")
    question
    if question in floor_rooms1:
        print(f"ok heading to floor {floors[0]}")
        people_in_elevator -=1
    elif question in floor_rooms2:
        print(f"ok heading to floor {floors[1]}")
        people_in_elevator -=1
    elif question in floor_rooms3:
        print(f"ok heading to floor {floors[2]}")
        people_in_elevator -=1
    else :
        print("incorrect input")

# break 
stop_light_on = True 
red_count = 30
green_count = 30
yellow_count = 30
light_color = [green_count,yellow_count,red_count]
while stop_light_on == True:
    if green_count == 30 

    while red_count == 30:
        red_count -= 1
        if red_count == 0 :
'''
