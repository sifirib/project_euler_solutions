def is_equal(dividend):
    numbers = []    

    for divider in range(10,100):
        elemans2 = []
        elemans1 = []
        str_dividend = str(dividend)
        str_divider = str(divider)
        a = str_dividend[0]
        b = str_dividend[1]
        c = str_divider[0]
        d = str_divider[1]
        elemans1.append(a)
        elemans1.append(b)
        elemans2.append(c)
        elemans2.append(d)
        if a or b == c or d:
            if  a or b or c or d == '0':
                continue
            else:
                if elemans1[0] == elemans2[0]:
                    elemans1.remove(elemans1[0])
                    elemans2.remove(elemans2[0])
                if len(elemans1) == 2 and len(elemans2) == 2 and elemans1[1] == elemans2[1]:
                    elemans1.remove(elemans1[1]) 
                    elemans2.remove(elemans2[1])
                if len(elemans1) == 2 and len(elemans2) == 2 and elemans1[0] == elemans2[1]:
                    elemans1.remove(elemans1[0])
                    elemans2.remove(elemans2[1])
                if len(elemans1) == 2 and len(elemans2) == 2 and elemans1[1] == elemans2[0]:
                    elemans1.remove(elemans1[1])
                    elemans2.remove(elemans2[0])
                 
                if dividend / divider == int(elemans1[0]) / int(elemans2[0]):
                    numbers.append(elemans1[0])
                    numbers.append(elemans2[0])
               
    return numbers

the_numbers = []
the_numberss = []
for dividend in range(10,100):
    aux_numbers = is_equal(dividend)    
    i = 2
    k = 0
    while i < 10:
        if len(aux_numbers) == 2:
            if int(aux_numbers[k]) %i == 0 and int(aux_numbers[k+1]) %i == 0:
                the_numbers.pop(k)
                the_numbers.pop(k+1)
                the_numbers.append(aux_numbers[k] / i)
                the_numbers.append(aux_numbers[k+1] / i)
                i = 2
            elif i == 9:
                the_numbers.append(aux_numbers[k])
                the_numbers.append(aux_numbers[k+1]) 
        i += 1
    the_numberss.extend(the_numbers)

answer = 1
for i in range(1,len(the_numberss),2):
    answer *= the_numberss[i]
print(answer)
