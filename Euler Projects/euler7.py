#10001 inci asal sayi ? 

import math 

def prime_check(x):
    is_prime = True
    
    for i in range(2,int(math.sqrt(x)+1),):
        if x %i == 0:
            is_prime = False
            break
    return is_prime
                     
prime_count = 0  
i = 3 #for more speed (2ser 2ser atlatmak icin 3,5,7... (cift sayilar asal olamaz!))
while True:
    if prime_check(i):
        prime_count += 1
    if prime_count == 1000000:
            print(i)
            break
    i += 2