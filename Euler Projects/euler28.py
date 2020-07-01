number = 3
accrual = 2
counter = 1
sum = 1

while True:
    for j in range(1,5):
        sum += number
        number += accrual
        
    accrual += 2
    counter += 2
    if counter == 1001:
        print(sum)
        break
    
    
