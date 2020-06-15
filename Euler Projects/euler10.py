#2milyona kadarki asal sayilarin toplami
import math

def prime_check(x):
    is_prime = True
    if x == 2:
        is_prime = True
    else:
        
        for i in range(2,int(math.sqrt(x))+1):
            if x %i == 0:
                is_prime = False
                break
        return is_prime
number = 2   
sum = 0     
while True:
    
    if prime_check(number):
        sum += number
    
    if number == 2000000:
        break
    number += 1

print(sum)       
    
        