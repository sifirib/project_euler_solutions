def d(x):
    dividers = list()
    for i in range(1,x//2 + 1):
        if x %i == 0:
            dividers.append(i)
    amicable = sum(dividers)
    return amicable

amicables = list()
for i in range(1,10001):
    amicable = d(i)

    if d(amicable) == i and i != amicable and i not in amicables:
        amicables.append(i)
        amicables.append(amicable)

theanswer = sum(amicables)
print(theanswer)        
        
    
    
          
    
        