# 1. Decisions at the Crossroad
number =int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")


# 2. The Story Brancher
choice = input("Do you choose the path to the left or right? ")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")


# 3. The Greatest Showdown
    # Task 1 
print("List three numbers")
number_1 = int(input("#:  "))
number_2 = int(input("#:  "))
number_3 = int(input("#:  "))

if number_1 > number_2 and number_1 > number_3: 
    print("The greatest number is: ")
    print(number_1)
elif number_2 > number_1 and number_2 > number_3: 
    print("The greatest number is: ")
    print(number_2)
elif number_3 > number_1 and number_3 > number_2: 
    print("The greatest number is: ")
    print(number_3)

    # Task 2
if number_1 < number_2 and number_1 < number_3: 
    print("The smallest number is: ")
    print(number_1)
elif number_2 < number_1 and number_2 < number_3: 
    print("The smallest number is: ")
    print(number_2)
elif number_3 < number_1 and number_3 < number_2: 
    print("The smallest number is: ")
    print(number_3)

    # Task 3 
if number_1 == number_2 and number_1 > number_3: 
    print("Two numbers are equal and the largest is: ")
    print(number_1)
elif number_2 > number_1 and number_2 == number_3: 
    print("Two numbers are equal and the largest is: ")
    print(number_2)
elif number_3 == number_1 and number_3 > number_2: 
    print("Two numbers are equal and the largest is: ")
    print(number_3)
elif number_3 == number_1 and number_3 == number_2 and number_1 == number_2: 
     print("All numbers are equal")


# 4. Leap Year Explorer
    # Task 1 
year = int(input("Pick a year: "))

if year % 4 == 0 and year % 400 == 0:
    print("It is a leap year!")
else: 
    print("It is not a leap year")

    # Task 2 
if year % 100 == 0 :
    print("It is a century year")

    # Task 3 
from datetime import datetime, date, time, timedelta

current_datetime = datetime.now()
current_year = current_datetime.year

if year > current_year:
    print(year," is in the future.")
elif year < current_year:
    print(year," is in the past.")
else:
    print(year, " is the current year.")