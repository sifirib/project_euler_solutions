
the_numbers = []    
    
for i in range(10,100):
    number_list1 = []
    number1 = i
    str_number1 = str(i)
    for a in range(0,2):
        if str_number1[a] not in number_list1 and str_number1[a] != 0:
            number_list1.append(str_number1[a]) # []
    
    for j in range(100,1000):
        number_list2 = []
        number2 = j
        str_number2 = str(j)
        for b in range(0,3):
            if str_number2[b] not in number_list2 and str_number2[b] != 0:
                number_list2.append(str_number2[b]) # []
        number_lists = number_list1
        number_lists.extend(number_list2)
        
        result = i * j
        str_result = str(result)
        for c in range(0,4):
            if str_result[c] not in number_lists and str_result[c] != 0:
                continue
                if i == 3 and result not in the_numbers:
                    the_numbers.append(result)
print(the_numbers)
for i in range(1,10):
    number_list1 = []
    number1 = i
    str_number1 = str(i)
    for a in range(0,1):
        if str_number1[a] not in number_list1 and str_number1[a] != 0:
            number_list1.append(str_number1[a]) # []
    
    for j in range(1000,10000):
        number_list2 = []
        number2 = j
        str_number2 = str(j)
        for b in range(0,4):
            if str_number2[b] not in number_list2 and str_number2[b] != 0:
                number_list2.append(str_number2[b]) # []
        number_lists = number_list1
        number_lists.extend(number_list2)
        
        result = i * j
        str_result = str(result)
        for c in range(0,4):
            if str_result[c] not in number_lists and str_result[c] != 0:
                continue
                if i == 3 and result not in the_numbers:
                    the_numbers.append(result)
print(the_numbers)
                                    
        

