#odd composite number can be written as the sum of a prime and twice a square.
#the conjecture is false
#what is the smallest odd composite number that cannot be written as sum of a prime number and twice a square?

def is_prime(x):
    for i in range(2,x):
        if x %i == 0:
            return False
            break
    return True
    
def is_canbe_written(x):
    for i in primes:
        for j in range(1,int(number ** 0.5) + 1):
            if i + 2 * (j ** 2) == x:
                return True
    return False
    
number = 3
primes = []
while True:

    if is_prime(number):
        primes.append(number)
    
    else:
        if is_canbe_written(number) == False:
            print(number)
            break
    
    
    
    
    
    
    
    
    
    
    
    number += 2
    