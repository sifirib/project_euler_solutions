def base10_to_base2(x):
    str_x = str(bin(x))
    core = []
    for i in range(2,len(str_x)):
        core.append(str_x[i])

    str_number = "".join(core)
    number = int(str_number)
    
    return number

def controller(string):
   reverse = int(string[len(string)::-1])
   if reverse == int(string):
       return True
   return False
   

the_list = []
for i in range(1,1000001):
    number = base10_to_base2(i)
    str_number = str(number)
    if controller(str_number) and controller(str(i)):
        the_list.append(i)
                
print(sum(the_list))