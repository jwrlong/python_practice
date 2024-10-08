# # Video: Python for Beginners - Learn Python in 1 hour
# # YC: Programing with Mosh

# #VARIABLE
# age = 20
# price = 19.95
# first_name= "Mosh"
# is_online = False
# print(age)

# # Exercise 1
# first_name = "John Smith"
# age = 20
# new_patient = True

# #TYPE CONVERSATION
# name = input("What is your name? ")
# print("Hello " + name)

# birth_year = input ("Enter your birth year: ")
# age = 2024 - int(birth_year)
# print(age)


# #important conversions:
# #int()
# #float()
# #bool()
# #str()

# #Exercise 2
# first = float(input("First: "))
# second = float(input("Second: "))
# total = str(first + second)
# print(total)

# #STRINGS
# course = 'Python for Beginners'
# print('Python' in course) #vs
# #print(course.find('Python'))


# #ARITHMETIC OPERATIONS
# #// means you do not get a float as an answer
# #/ dividing, but you get a float as an answer
# #+, -, *, ** you know what these are, you are a smart girl

# #COMPARISON OPERATORS
# #the following is a boolean expression
# #x = 3 > 2
# # a double "==" is saying something is absolute
# #x = 3 == 2
# # a "!=" is saying something is not equal
# #x = 3 != 2
# #here are some others: >, >=, <, <=, ==, !=

# #LOGICAL OPERATORS: and, not, or
# price = 25
# print(price > 10 and price < 30)


# #Exercise: Weight Converter (My solution)
# weight = input("Weight: ")
# metric = input("(K)g or (L)bs: ")
# weightL = float(weight)*.453
# weightK = float(weight)* 2.20462

# if metric == 'L' or 'l':
#     print ("Weight in Kg: " + str(weightL))
# elif metric == 'K' or 'k': 
#     print ("Weight in Lbs: " + str(weightK))
    
# # Exercise: Weight Converter (ChatGPTs solution)
# weight = float(input("Weight: "))
# metric = input("(K)g or (L)bs: ")

# if metric.lower() == 'l':
#     weight_in_kg = weight * 0.453592  # Convert lbs to kg
#     print(f"Weight in kg: {weight_in_kg}")
# elif metric.lower() == 'k':
#     weight_in_lbs = weight * 2.20462  # Convert kg to lbs
#     print(f"Weight in lbs: {weight_in_lbs}")
# else:
#     print("Please enter a valid metric (K for kilograms or L for pounds).")


#WHILE LOOPS
# i = 1
# while i <= 10:
#     print(i * '*') #you cannot concatonate a int with a string... but this is different
#     i = i + 1
    
# #LIST
# 1
# 1.1
# True
# 'a'

# names = ["John", "Bob", "Mosh", "Sam", "Mary"]
# # print(names[0])

# #Lets update the name John on the list
# names[0] = "Jon" 
# print(names)
# print(names[0:3]) #we are slicing a piece of the list

# #LIST METHODS
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6) #adds the number 6 to the list
# numbers.insert(0,-1) #we are inserting a specific value at a certain spot
# numbers.remove(3)#we're removing a specific item
# numbers.clear()#we are clearing the whole list
# print(1 in numbers)#this allows us to determine if a specific item is in a list

# print(len(numbers))#returns the number of elements in a list

# #FOR LOOPS
# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# #example of a for loop
# for item in numbers: #this is called a for loop. for each iteration, the item is holding each value in the list
#     print(item)

# i = 0 #this is the same thing as the above, but this is more complicated and less efficient
# while i < len(numbers):
#     print(numbers[i])
#     i = i+1

# #the following demonstrates a range of ways to use the for loops with range function
# numbers = range(5)
# print(numbers)

# numbers = range (5, 10, 2)
# for number in numbers:
#     print(number)

# for number in range(5): #another alternative!!
#     print(number)
    

#TUPLES: kinda like lists, but we cannot change them (immutable)
numbers = (1, 2, 3, 4, 5)
#if you were to try to modify the above list, you would run into an error message
