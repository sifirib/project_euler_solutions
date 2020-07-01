numbers = []
for i in range(2,1000000):
    str_number = str(i)
    tot = 0
    for k in range(0,len(str_number)):
        int_number = int(str_number[k])
        tot += int_number ** 5
    if tot == i:
        numbers.append(i)

print(sum(numbers))
        