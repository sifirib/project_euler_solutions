
# import sympy

# the_longest = 0
# for a in range(-1000,1000):
#     for b in sympy.primerange(1, 1000):
#         longest = 0
#         n = 0
#         while sympy.isprime(n**2 + a*n + b):
#             longest += 1
#             n += 1
#             if longest > the_longest:
#                 the_longest = longest
#                 am = a  
#                 bm = b
# print(am * bm)

#solution 2 (faster)

def is_prime(x):
    for i in range(2,int(x**0.5) + 1):
        if x %i != 0:
            return True
        else:
            return False
        
        
the_longest = 0
for a in range(-1000,1000):
    for b in (1, 1000):
        if is_prime(b):
            longest = 0
            n = 0
            while is_prime(n**2 + a*n + b):
                longest += 1
                n += 1
                if longest > the_longest:
                    the_longest = longest
                    am = a  
                    bm = b
print(am * bm)