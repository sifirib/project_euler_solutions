#28123 den küçük olup 2 abundant sayının toplamıyla yazılamayacak! sayıların toplamı kaçtır
#abundant sayılar pozitif bölenlerinin toplamı kendinden büyük olan sayılardır
import math

def abundant_finder(x):
    sum = 1
    i = 2
    while(i < math.ceil(math.sqrt(x))): #math.ceil sayıyı yukarı yuvarlar mesela 4.5 sayısını 5 e yuvarlar.
        
        if x %i == 0:
            if i*i == x:
                sum += i
                i += 1
            else:    
                sum += i
                sum += x // i
            
        i += 1
        
    if sum > x:
        return x
       
numbers = list()        
  
for i in range(1,28124):
    # print(f"{i}")
    aux = 0
    for j in range(1,i//2 + 1):
        if abundant_finder(j):
            # print(f" {j}")
            for k in range(1,i - j + 1):
                if abundant_finder(k):
                    # print(f"   {k}")
                    if i == j + k:
                        if i not in numbers:
                            numbers.append(i)
                            continue
                    else:
                        continue
    
sum1 = sum(numbers)
sum2 = 28123*28124/2                
print(int(sum2 -sum1))      
 
