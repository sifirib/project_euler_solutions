
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?


def dig_summer(i):
    sum = 0
    i = str(i)
    for j in range(0,len(i)):
        k = int(i[j])
        sum += k
    return sum
dig_summer(2**1000)
        
    