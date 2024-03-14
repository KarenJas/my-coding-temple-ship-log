''' 1. The Username Validatr
username = input("username: ")
    #username is karenkaren

if len(username) == 10 :
    print ("welcome back!")
else: 
    print("Incorrect Username :(")
'''

'''2. The previse Price Tagger
prices = [3.523,4.224,6.865]
rounded_prices = [ ]
for price in range(len(prices)):
    rounded= round(prices[price],2)
    rounded_prices.append(rounded)
print(rounded_prices)
'''

'''3. Global Temperature Translator
adjective = "sunny"
temperature = 80
print(f"Cant believe its {temperature} degrees outside. Its so {adjective} :) ")
'''

'''4. The Goldilocks Room Selector

temperatures_of_the_day = [50,60,70,47,63,57,75]

if min(temperatures_of_the_day) > 65:
    print(f"it was pretty warm in here today, {min(temperatures_of_the_day)} degrees. :(")
else: 
    print(f"It was nice and chilly in here, {max(temperatures_of_the_day)} degrees. :)")
'''

'''5. The E-commerce Cart Summary
#item1 = [{"price" : 27.53, "Stock Status" : "Out of Stock"}]
#item2 = [{"price" : 50.77, "Stock Status" : "In Stock"}]
#item3 = [{"price" : 19.99,"Stock Status" : "In Stock"}]
#cart = []
#print(item1)
#print(item2)
#print(item3)

item1_price = 22
item1_status = "in stock"
print("item1 price: ",item1_price,"\titem1 status: ", item1_status)
'''

'''9. the type inspector challenge
list = [1,'HI',4.67,True]
for i in range(len(list)):
    if type(list[i]) == int:
        print(list[i],"is an int:",isinstance(list[i], int))
    elif type(list[i]) == str:
        print(list[i],"is a str:",isinstance(list[i], str))
    elif type(list[i]) == float:
        print(list[i],"is a float: ",isinstance(list[i], float))
    elif type(list[i]) == bool:
        print(list[i],"is a bool:",isinstance(list[i], bool))
    '''

'''10. The Match Function Marathon'''
import math
list = [1,2,3,4,5.89,6]
sum(list)
print("sum:",sum(list))
print("round:",round(list[4]))
print(sqrt)
