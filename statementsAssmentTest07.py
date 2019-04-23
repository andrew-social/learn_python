#Statements Assessment Test
#Let's test your knowledge!

#Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
#Code here
for test in st.split():
	if test[0] == 's':
		print(test)
#Code here
#Use range() to print all the even numbers from 0 to 10.

#Code here
for x in range(1,11):
	print(x)
#Code here
#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

#Code here
print([num for num in range(1,51) if num % 3 == 0])
#Code here
#Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
#Code here
for mystring in st.split():
	if len(mystring)%2==0:
		print(mystring+' even')
#Code here
#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
#and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

#Code here
for num in range(1,101):
	if num%3 == 0 and num %5 == 0:
		print('FizzBuzz')
	if num%3 == 0:
		print('Fizz')
	if num%5 == 0:
		print('Buzz')


#Code here
#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
#Code here
print([x[0] for x in st.split()])
#Code here
