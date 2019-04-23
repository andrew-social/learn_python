# Python 3 Cheat Sheet

# Data types
# Strings
# Numeric:
#	Integer
#	Float
# Lists
# Tuples
# Dictionaries

# Examples
# Strings
myString = 'abcdefghijklmnopqrstuvwxyz'
words = 'this is a short sentance'
# Numeric
myInteger = 100
MyFloat = 10.5


# Lists: Lists can contain any datatype
myListStrings = ['123', '456', '789']
myListNumeric = [2, 3, 4, 5, 6]
myListMixed = [1, 'abc', ['123', '456', '789']]

print('------------------------------------------------------------------')
#Create a list of all numbers between 1 and 50, by using the .append method.
mylist=[]
for i in range(1,51):
		mylist.append(i)
print(mylist)

#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print([i for i in range(1,51) if i%3 == 0])

# Methods associated with lists
#List methods
names = ["Larry", "Curly", "Moe"]
print(names)
# append element to the end
names.append("Shemp")
print(names)
# insert element at index 0
names.insert(0, "Carlin")
print(names)
# add list of elements at end
names.extend(["Williams","Yankovic"])
print(names)
# Print index 2
print(names[1])
print('------------------------------------------------------------------')

#Test if a value is contained in a list
names = ["Larry", "Curly", "Moe"]
#Check if name exists
if "Curly" in names:
	print ("Yea")
else:
	print("Boo")
print('------------------------------------------------------------------')

# Tuples
myTuple = ('abc', 'def', 'ghi')

# Dictionaries: Dictionaries contain Key:Value pairs
myDict = {'student1':'Kevin', 'student2':'Mary'}

print('------------------------------------------------------------------')
# Loops
# For/in loops
# Print every character in string
for testVar in myString:
	print(testVar)
print('------------------------------------------------------------------')

# Print every word in string
for testVar in words.split():
	print(testVar)
print('------------------------------------------------------------------')

# Print first letter of each word
for testVar in words.split():
	print(testVar[0])
print('------------------------------------------------------------------')

# Print words starting with 's'
print('Print words starting with \'s\'')
for testVar in words.split():
	if testVar[0] == 's':
		print(testVar)

print('------------------------------------------------------------------')

#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
print([x[0] for x in st.split()])

print('------------------------------------------------------------------')

# Traditional numeric for loop
# Loop through the numbers 1 to 100
print('Traditional numeric for loop')
for testVar in range(1,101):
	print testVar
print('------------------------------------------------------------------')

# Traditional numeric for loop as a list comprehension
print('Traditional numeric for loop as a list comprehension')
print([testVar for testVar in range(1,101)])
print('------------------------------------------------------------------')

# Print all numbers between 1 and 50 that are divisible by 3.
for i in range(1,51):
	if i % 3 == 0:
		print (i)
print('------------------------------------------------------------------')

#Create a list of all numbers between 1 and 50 that are divisible by 3.
mylist=[]
for i in range(1,51):
	if i%3==0:
		mylist.append(i)
print(mylist)
print('------------------------------------------------------------------')

#Use List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print([i for i in range(1,51) if i%3 == 0])

print('------------------------------------------------------------------')

# Print every word in a string that has an even number of letters
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
	if len(word)%2 == 0:
		print(word+' <-- Even')
print('------------------------------------------------------------------')

#Print every word of the string below. If the word is even print "even!", or odd, print "odd"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
	if len(word)%2==0:
		print(word+" Even")
	else:
		print(word+" Odd")
print('------------------------------------------------------------------')

#Write a program that prints the integers from 1 to 100. But for multiples of 
#three print "Fizz" instead of the number, 
#and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,101):
	if i%3 and i%5 == 0:
		print("FizzBuzz")
	if i%3 == 0:
		print("Fizz")
	if i%5 == 0:
		print("Buzz")
	print(i)
print('------------------------------------------------------------------')

#Calculate prime numbers in a range and store in a list
prime = []
for val in range(1, 9999 + 1): 
   # If num is divisible by any number   
   # between 2 and val, it is not prime  
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           prime.append(val)
print(prime)

print('------------------------------------------------------------------')

#Iterate through string, and append each element into list
mystring = 'hello'

mylist = []
for letter in mystring:
	mylist.append(letter)
print(mylist)

#How to do the same thing in list comprehension
mylist = [letter for letter in mystring]
print(mylist)

#To populate a list with integers
numlist = [num for num in range(0,11)]
print(numlist)

#To perform a mathmatical operation on the numbers to go into the list,
#For example to square every number
numlist = [num**2 for num in range(0,11)]
print(numlist)

#To use an if statement, for example to only process the even numbers
numlist = [num for num in range(0,11) if num%2 == 0]
print(numlist)

#Combine both techniques, get the square of the even numbers
numlist = [num**2 for num in range(0,11) if num%2 == 0]
print(numlist)

#To convert Centigrade to fahrenheit, put the formula in the begining, and the list of temps at the end
celcius = [0, 10, 20, 34.5]
fahrenheit = [( (9/5)*temp + 32) for temp in celcius]

print(fahrenheit)
#Note: calcuations are wrong when using Sublime compares to cli Python

#To unflaten the list comprehension to the full for loop
celcius = [0, 10, 20, 34.5]
fahrenheit = []

for temp in celcius:
	fahrenheit.append(( (9/5)*temp + 32))

print(fahrenheit)
#Note Python has more strict formatting rules than Sublime

#To nest for loops
mylist = []

for x in [2,4,6]:
	for y in [1, 10, 100]:
		mylist.append(x*y)

print(mylist)

#To flatten as a list comprehension at the loss of readability
mylist = [x*y for x in [2,4,6] for y in [1, 10, 100]]
print(mylist)

print('------------------------------------------------------------------')

#Generate list of X numbers, randomize, and sort
import random
numLow=1
numHigh=1000000
#Generate list of numbers from 1 to 10,000
data = list(range(numLow, numHigh+1))
print('Randomizing ' + str(numHigh) + ' numbers')
random.shuffle(data)
#print(data)
print('Reverse sorting ' + str(numHigh) + ' numbers')
data.sort(reverse = True)
#print(data)
print('Forward sorting ' + str(numHigh) + ' numbers')
data.sort()
#print(data)

print('------------------------------------------------------------------')

# List of methods 
#Method			Description
#List append()	Add Single Element to The List
#List insert()	Inserts Element to The List
#List remove()	Removes Element from the List
#List index()	returns smallest index of element in list
#List count()	returns occurrences of element in a list
#List pop()		Removes Element at Given Index
#List reverse()	Reverses a List
#List sort()		sorts elements of a list
#List copy()		Returns Shallow Copy of a List
#List clear()	Removes all Items from the List
#List extend()	Add Elements of a List to Another List
#any()			Checks if any Element of an Iterable is True
#all()			returns true when all elements in iterable is true
#ascii()			Returns String Containing Printable Representation
#bool()			Converts a Value to Boolean
#enumerate()		Returns an Enumerate Object
#filter()		constructs iterator from elements which are true
#iter()			returns iterator for an object
#list() Function	creates list in Python
#len()			Returns Length of an Object
#max()			Returns largest element
#min()			Returns smallest element
#map()			Applies Function and Returns a List
#reversed()		Returns reversed iterator of a sequence
#slice()			Creates a slice object specified by range()
#sorted()		Returns sorted list from a given iterable
#sum()			Add items of an Iterable
#zip()			Returns an Iterator of Tuples

print('------------------------------------------------------------------')

# Comparison operators
print(1 == 1)
print(1 != 2)
print(2 > 1)
print(1 < 2)

# Logical operators
print(1 == 1 and 1 != 2)
print(1 == 1 or 1 == 2)
print(not(1 == 2))

print('------------------------------------------------------------------')

# Control flow
#if some_condition:
#    execute some code
#elif some_other_condition:
#    do_something_different
#else:
#    do_something_else

i = 10
if i > 20:
	print('i is less than 20')
elif i > 15:
	print('i is less than 15')
else:
	print('i=10')

# Loops
# my_iterable = [1,2,3]
# for item_name in my_iterable:
#    print(item_name)

mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
	print(num)

#Print even numbers in list
for num in mylist:
	if num % 2 = 0
		print(f'Even'+num)
	else:
		print(f'Odd'+num)

# Running tally
list_sum = 0
for num in mylist:
	list_sum = list_sum + num

print(list_sum)


myString = 'hello world'

for letter in myString:
	print(letter)

print('------------------------------------------------------------------')

#Tuple unpacking
mylist = [(1,2),(3,4),(5,6),(7,8)]
len(mylist)
# Regular iterate over list
for item in mylist:
	print(mylist)

# Tuple unpacking
for (a,b) in mylist:
	print(a)
	print(b)

mylist = [(1,2,3),(4,5,6),(7,8,9)]
for a,b,c in mylist:
	print(b)

