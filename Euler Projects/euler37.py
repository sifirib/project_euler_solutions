import math

def is_prime(x):  
    for i in range(2,int(math.sqrt(x)) + 1):
            if x %i == 0:
                return False
                break
    if x == 1 or x == 0:
        return False
    return True


def l_to_r(x):
    str_x = str(x)  
    figures = list("".join(str_x))
    for i in range(1,len(str(x))):
        figures.pop(0)
        new_number = int("".join(figures))
        if is_prime(new_number):
            k = 1
        else:
            k = 0
            break
    if k == 1:
        k = 0
        return True
    else:
        return False

def r_to_l(x):
    str_x = str(x)    
    figures = list("".join(str_x))
    for i in range(1,len(str(x))):
        figures.pop(-1)
        new_number = int("".join(figures))
        if is_prime(new_number):
            k = 1
        else:
            k = 0
            break
    if k == 1:
        k = 0
        return True
    else:
        return False

i = 8
the_list = []
while len(the_list) <= 10:
    if is_prime(i):
        if r_to_l(i) and l_to_r(i):
            the_list.append(i)   
    i += 1       

print(sum(the_list))