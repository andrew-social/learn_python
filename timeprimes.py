def approach1(givenNumber):

    # Initialize a list
#    print("givenNumber = ", givenNumber)
    primes = []
    for possiblePrime in range(2, givenNumber + 1):
        # Assume number is prime until shown it is not
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False

        if isPrime:
            primes.append(possiblePrime)
        return(primes)
    #print (primes)

def approach2(givenNumber):

    # Initialize a list
    primes = []

    for possiblePrime in range(2, 9999):
        # Assume number is prime until shown it is not
        isPrime = True
        for num in range(2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(possiblePrime)
        return(primes)
    #print (primes)

def testFunction(var1):
    return(var1)

import timeit

# Approach 1: Execution time
print(timeit.timeit('approach1(50000)', globals=globals(), number=1000000))
#print(timeit.timeit('testFunction(12345)'))
# print(timeit.timeit('approach1(500)', globals=globals(), number=1000000))
#print(timeit.timeit('approach2(500)', globals=globals(), number=1000000))
