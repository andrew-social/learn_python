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

print (primes)

