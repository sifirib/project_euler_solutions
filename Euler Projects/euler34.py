
def factorial(x):
    fact = 1
    for i in range(1,x + 1):
        fact *= i 
    return fact

the_list = []
number = 3

while True:
    aux = 0
    str_number = str(number)
    for i in str_number:
        aux += factorial(int(i))
    if aux == number:
        the_list.append(number)
    
    number += 1
    
    if 362880 * len(str_number) < number: # (9! * len(str_number) )
        break
            
print(sum(the_list))    









   