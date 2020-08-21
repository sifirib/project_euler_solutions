def is_prime(x):
    for i in range(2,int(x**0.5) + 1):
        if x %i == 0:
            return False
            break
    return True

largest = 0
for i in range(10000001,0,-2):
    if is_prime(i):
        stri = str(i)
        figures = set()    
        for j in range(1,len(stri) + 1):
            figures.add(str(j))
    
        if set(stri) == figures:
            print(i)
            break


##           SOLUTION 2 (optimized!)
# import itertools
         
# def is_prime(x):
#     for i in range(2,int(x**0.5) + 1):
#         if x %i == 0:
#             return False
#             break
#     return True

# figures = '1234567'
# numbers = list(itertools.permutations(figures))
# numbers.sort(reverse = True)

# largest = 0
# for number in numbers:
#     number = "".join(number)
#     if is_prime(int(number)):
#         print(number)
#         break

