i = 0
figures = set("123456789")
the_list = []
while i < 9999:
    i += 1
    number = i
    j = 2
    str_number = str(number)
   
    while True:
        
        str_number += str(number * j) # probably the line that causes the problem is this
        l = 0
        if len(str_number) >= 9:
             if len(str_number) > 9:
                 break   
             else:
                 if set(str_number) == figures:
                    the_list.append(int(str_number))
                    break
                      
        j += 1      
     
print(max(the_list))