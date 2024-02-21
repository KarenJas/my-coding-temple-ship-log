# 1. Python List Transformation
    # Task 1 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

    # Task 2
total_of_grades = sum(grades)
number_of_items = len(grades)
average_of_grades = total_of_grades/number_of_items
print(average_of_grades)

    #Task 3
grades.remove(78)
grades.insert(7,"Failed")
grades.remove(76)
grades.insert(8,"Failed")
grades.remove(72)
grades.insert(9,"Failed")
print(grades)


#2. Advanced List Methods and Identity Operators
    # Task 1 
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]#eve and frank
submitted_attented = []

if submitted[0] in attended :
    submitted_attented.append(submitted[0])

if submitted[1] in attended :
    submitted_attented.append(submitted[1])


if submitted[2] in attended :
    submitted_attented.append(submitted[2])


if submitted[3] in attended :
    submitted_attented.append(submitted[3])
   

print(f"The kids that have submitted their homework and attended class are: {submitted_attented}")

    # Task 2
identical_or_not = submitted is attended
if identical_or_not == True:
    yes_no = "yes"
else :
    yes_no = "no"
print(f"Are the Two lists identical?: {yes_no}")

    # Task 3
if attended[0] not in submitted :
    attended.remove(attended[0])

if attended[1] not in submitted :
    attended.remove(attended[1])

if attended[1] not in submitted :
    attended.remove(attended[1])

if attended[2] not in submitted :
    attended.remove(attended[2])

print(attended)


# 3. Advanced Slicing Techniques
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
    # Task 1 
second_week = temperatures [13:20]
print(second_week)
    # Task 2 
above_100 = temperatures [24:]
print(above_100)
    # Task 3
temperatures.sort(reverse=True)
fifth_to_tenth = temperatures [4:9]
print(fifth_to_tenth)


# 4. List Comprehensions and Membership Operators
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = numbers.copy()
    # Task 1
even_numbers = []
if numbers[0] % 2 == 0:
    even_numbers.append(numbers[0])

if numbers[1] % 2 == 0:
    even_numbers.append(numbers[1])

if numbers[2] % 2 == 0:
    even_numbers.append(numbers[2])

if numbers[3] % 2 == 0:
    even_numbers.append(numbers[3])

if numbers[4] % 2 == 0:
    even_numbers.append(numbers[4])

if numbers[5] % 2 == 0:
    even_numbers.append(numbers[5])

if numbers[6] % 2 == 0:
    even_numbers.append(numbers[6])

if numbers[7] % 2 == 0:
    even_numbers.append(numbers[7])

if numbers[8] % 2 == 0:
    even_numbers.append(numbers[8])

if numbers[9] % 2 == 0:
    even_numbers.append(numbers[9])
print(even_numbers)

    # Task 2
greater_than_5 = [x for x in numbers if x > 5]
print(greater_than_5)
    # Task 3 
number_7 = numbers_2.count(7)
print(number_7)


# 5. Deep Dive into Python Lists
    # Task 1 
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
school_data = [ ]

for i in range(len(students)):
    school_dic = {"name": students[i], "grade": grades[i], "activity": activities[i]}
    school_data.append(school_dic)

print(school_data)
   
    # Task 2 
for i in range(len(grades)-1):
    if grades[i] < 80:
        del school_data[i]
        
print(school_data)

    # Task 3 
for students in school_data:
    students["status"] = "Passed"

print(school_data)


        