
perimeters = dict()# for example 1st perimeter includes 3 possibilities(its not true) to make a right triangle, in that case the value of dictionary for (perimeter = 1) is 3. (1:3)
for a in range(333,501): # variable of a doesnt must be less than 333 due to its the longest edge and any length of edges dont must be higher than 500  
    for b in range(1,1001 - a):
        for c in range(1,1001 - a - b):
            perimeter = a + b + c
            if a**2  == b**2 + c**2:
               if perimeter in perimeters:
                   perimeters[perimeter] += 1
               else:
                   perimeters[perimeter] = 1
                           
for k,v in perimeters.items():
    if v == max(perimeters.values()):
        print(k)
        
        
        
        
## SOLUTION 2 (double optimized!)
        
# for b in range(1,500):
#     for c in range(1,500):
#         a = (b**2 + c**2) ** 0.5
#         if a + b + c > 100:
#             break
#         else:
#             if a == int(a):
#                 perimeter = int(a) + b + c
#                 if perimeter in perimeters:
#                     perimeters[perimeter] += 1
#                 else:
#                     perimeters[perimeter] = 1
    
# for k,v in perimeters.items():
#     if v == max(perimeters.values()):
#         print(k)
                