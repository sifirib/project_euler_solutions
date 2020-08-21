
# LITERALLY SHIT (the method of creating number must be better than this literal shit, in the func side there is no problem)
# (it can calculate the answer but itll take so many hours)

# def is_suitable(x):
#     aux_figures = list()
#     for i in str(x):
#         if i in str(aux_figures):
#             return False
#             break
#         aux_figures.append(i)
#     strx = str(x)
#     if int(strx[1]+strx[2]+strx[3]) %2 == 0:
#         if int(strx[2]+strx[3]+strx[4]) %3 == 0:
#             if int(strx[3]+strx[4]+strx[5]) %5 == 0:
#                 if int(strx[4]+strx[5]+strx[6]) %7 == 0:
#                     if int(strx[5]+strx[6]+strx[7]) %11 == 0:
#                         if int(strx[6]+strx[7]+strx[8]) %13 == 0:
#                             if int(strx[7]+strx[8]+strx[9]) %17 == 0:
#                                 return True
        
# thelist = []
# for number in range(1023456789,9876543211):
#     if is_suitable(number):
#         thelist.append(number)

# print(sum(thelist))

## SECOND SOLUTION (optimized)
import itertools

digits = "0123456789"
numbers = itertools.permutations(digits)
numberlist = ["".join(number) for number in numbers if not number[0] == "0"]

summ = 0
primes = [2,3,5,7,11,13,17]

for number in numberlist:
    is_ok = True
    
    for i in range(7):
        if int(number[i + 1:i + 4 ]) %primes[i] != 0:
            is_ok = False
            
    if is_ok:
        summ += int(number)

print(summ)        
































        