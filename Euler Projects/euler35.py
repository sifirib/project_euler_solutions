import math
def is_prime(x):
    for i in range(2,int(math.sqrt(x)) + 1):
        if x %i == 0:
            return False
            break
    return True

the_numbers = []
for number in range(2,1000000):
    if is_prime(number):
        
        liste = []
        str_number = str(number)
    
        for j in str_number:
            liste.append(j)
        
        pop = liste.pop(-1)
        liste.insert(0,pop)
        k = 1
        for i in range(1,len(liste)):
            
            aux = "".join(liste)
            if is_prime(int(aux)):
                pop = liste.pop(-1)
                liste.insert(0,pop)
                k += 1
            
            else:
                break
          
        if k == len(liste) and number not in the_numbers:
            the_numbers.append(number)

print(len(the_numbers))
print(the_numbers)
