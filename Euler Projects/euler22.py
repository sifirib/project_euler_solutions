import string
alphabets = list(string.ascii_uppercase)

with open("/home/hrx/Desktop/projects/python/Euler Projects/names.txt") as f:
    names = f.read()
names = names.split(",")
list.sort(names)

names2 = []
for i in names:
    names2.append(i[1:len(i)-1]) # for remove the quotation marks

def letter_number_sum(name):
    letter_number = 0 
    for i in range(0,len(name)):
        letter_number += alphabets.index(name[i]) + 1
        
    return letter_number

def name_number(name,list):
    name_number = names2.index(name) + 1
    return name_number

sum = 0
for i in names2:
    
    a = letter_number_sum(i) 
    b = name_number(i,names2)
    sum += a*b

print(sum)
    