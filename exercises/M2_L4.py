# utilize for loops to iterate over multiple lists and organize event details without using functions 
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
'''need to redo this and assign each kid their individual seat'''