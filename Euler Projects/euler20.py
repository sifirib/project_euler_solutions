def factorial(x):
    fact = 1
    for i in range(1,x+1):
        fact *= i
    return fact

str_fact = str(factorial(100))
sum = 0

for i in str_fact:
    sum += int(i)
print(sum)    

    