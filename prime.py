prime = []
for val in range(1, 99999 + 1): 
   # If num is divisible by any number   
   # between 2 and val, it is not prime  
   if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           prime.append(val)
print(prime)