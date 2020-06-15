#solution1

# fibonacci_list = []
# fibonacci_list.append(1)
# fibonacci_list.append(1)
# cfibonacci_list = []

# for i in range(1,1000000000):
#     fibonacci_list.append(fibonacci_list[i] + fibonacci_list[i-1])
#     if fibonacci_list[i+1] >= 4000000:
#         fibonacci_list.pop()
#         break

# for j in fibonacci_list:
#     if j % 2 == 0:
#         cfibonacci_list.append(j)

# print (sum(cfibonacci_list))




# solution2

# a = 1
# b = 1
# sum = 0

# while True:
#     c = a + b
#     a = b
#     b = c
    
#     if c > 4000000:
#         break
#     if c % 2 == 0:
#         sum += c
        
        
# print(sum)
