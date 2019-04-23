def testFunction(var1):
    return(var1)

import timeit
print(testFunction(12345))
print(timeit.timeit(testFunction(12345)))
