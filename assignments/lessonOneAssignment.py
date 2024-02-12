 #1.) Python Indentation Practice with if Statements

   # Task 1
weather = "sunny"

if weather == "sunny":
    print("Wear sunglasses!")
else :
    print("Take an umbrella")

    # Task 2
print("How do you feel today?") 
mood = "happy"

if mood == "happy":
    print("That's great to hear!")
if mood == "sad":
    print("I hope your day gets better!")

    # Task 3 
mood = "excited"

if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Lets find something fun to do!")


#2.) Python Comments & Multi-line Practice
  
    # Task 1
# Python, oh Python, so clear and so neat
# With every new challenge, you're hard to beat.
# Python, oh Python, a language to gain,
# Syntax and logic, like a newfound terrain.
# In the coding journey, you're my tutor, my lane.
    
    # Task 2 
'''
Python, in the realm of code you shine,
With simplicity and grace, you're truly divine.
In the realm of code, Python takes flight,
Simplicity and power, woven tight.
A language divine, in elegance dressed,
With every line, it proves the best.
In the coding cosmos, Python's zest.
'''

    # Task 3 
# This line is from my first poem 
# In the coding journey, you're my tutor, my lane.

# This line is from my multi-line poem 
'''
A language divine, in elegance dressed,
With every line, it proves the best.
'''


# 3.) Python Naming Convention Practice
    
pi_value = 3.14
userAge = 25
user_location = "New York"
MAXLIMIT = 1000


# 4.) Python Data Types and type() Function

variable_a = "Hello, World!"
print(type(variable_a))
variable_b = 23
print(type(variable_b))
variable_c = 3.14
print(type(variable_c))
variable_d = True
print(type(variable_d))


# 5.) Python Dynamic Typing Practice

dynamic_variable = "This is a string"
print(type(dynamic_variable))
dynamic_variable = 100
print(type(dynamic_variable))
dynamic_variable = 25.5
print(type(dynamic_variable))


# 6.) Arithmetic Operations in Daily Life

    # Task 1
apple = 1.5
ham = 3
bread = 2
total_cost = apple + ham + bread 
print(total_cost)

    # Task 2 
initial_amount = 1000
intrest_rate = .0435
year_savings = 1000 * (1+.0435)**1
print(year_savings)

    # Task 3 
width = 5
length = 10 
area = width * length 
print(area)
perimeter = 2 * (width + length)
print(perimeter)


#7.) Understanding Assignments and Comparisons

    # Task 1 
a = 5
b = 10
a, b = b, a
print("After swap: a =", a, "b =", b)

    # Task 2 
def is_perfect_square(number):
    square_root = (number ** 0.5)
    return square_root**2 == number
number_to_check = 82
result = is_perfect_square(number_to_check)
if result:
    print(number_to_check)
    print("is a perfect square.")
else:
    print(number_to_check)
    print("is not a perfect square.")


# 8.) Exploring Logical Operations and Precedence

    # Task 1 
value_1 = True
value_2 = False
value_3 = True

result_and = value_1 and value_2 and value_3
print("Result of AND operation: ")
print(result_and)
result_or = value_1 or value_2 or value_3
print(f"Result of OR operation: ")
print(result_or)
result_not = not value_1
print(f"Result of NOT operation: ")
print(result_not)

    # Task 2
expression_result_normal = 7 + 5 * 2
expression_result_with_parentheses = (7 + 5) * 2

if expression_result_normal == expression_result_with_parentheses:
    print("The results match!")
else:
    print("The results do not match.")

    # Task 3 
# Expression: (7 + 5 * 2) > 10 and (9 - 4) == 5
# Prediction:
#  (7 + 5 * 2) = 24
#  24 > 10 is True
#  (9 - 4) = 5
#  5 == 5 is True
#  True and True is True
    
result = (5 + 3 * 2) > 10 and (7 - 2) == 5
print("Prediction: True")
print(f"Actual result: ")
print(result)

