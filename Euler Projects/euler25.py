#1 1 2 3 5 8 13 21...
#What is the index of the first term in Fiboanacci sequence to contain 1000 digits?

i = 1
k = 1
step = 2

while True:
    i, k = k, i + k
    step += 1
    
    if len(str(k)) == 1000:
        print(step)
        break
    
    