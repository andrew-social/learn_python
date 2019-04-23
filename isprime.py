import timeit

def isprime1(n):
    for x in range(2,n):
#        print (n)
        if n % x == 0:
            return False
        return True
def isprime2(n):
    for x in range(2,n):
#        print (n)
        for num in range (2, int(x ** 0.5) + 1):
            if n % x == 0:
                return False
            return True
#    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not.
#        isPrime = True
#        for num in range(2, int(possiblePrime ** 0.5) + 1):
#            if possiblePrime % num == 0:
#            isPrime = False

#print ("1")
#print ([x for x in range(1,1000000) if isprime1(x)])
#[x for x in range(1,1000000) if isprime1(x)]
#print ("2")
#print ([x for x in range(1,1000000) if isprime2(x)])
#[x for x in range(1,1000000) if isprime2(x)]
#print ("Done")

print(timeit.timeit('[x for x in range(1,500) if isprime1(x)]', globals=globals(), number=10000))
print(timeit.timeit('[x for x in range(1,500) if isprime2(x)]', globals=globals(), number=10000))
#print(timeit.timeit('isprime2(500)', globals=globals(), number=10000))

#print (isprime(9))

#count = 0
#while (count < 9):
#    count = count + 1
#    print(isprime(count))
