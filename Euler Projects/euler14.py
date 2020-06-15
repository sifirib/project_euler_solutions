# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

# #solution1 (unoptimized!)
#def collatz(x):
#     if x %2 == 0:
#         return x/2
#     else:
#         return x * 3 + 1
    
# def steps(x):
#     step = 1
#     while True:
#         x = collatz(x)
#         step += 1
#         if x == 1:
#             return step
# answer = 0
# largest_step = 0

# for i in range(1,1000001):
#     aux = steps(i)      
#     if aux > largest_step:
#         largest_step = aux
#         answer = i
# print(answer)

#solution2 (optimized) 
import time
past_numbers = dict() #this dictionary includes numbers of steps of collatz sequences that already defined 

def collatz(number,past_numbers):
    given = number
    steps = 1
    while number != 1:
        
        if given in past_numbers:
            steps += past_numbers[number] - 1 # -1 because of number itself
            break
        if number %2 == 0:
            number //= 2
            steps += 1
        else:
            number = number * 3 + 1
            steps += 1
        
    past_numbers[given] = number
    return steps


answer = 1
largest_step = 1

start = time.time()
for i in range(1,1000001):
    aux = collatz(i,past_numbers)
    if aux > largest_step:
        largest_step = aux
        answer = i
finish = time.time()
print(f"it takes {finish - start} seconds ")
print(answer)
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
