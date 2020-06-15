#3 basamakli 2 sayinin carpimindan olusan en buyuk polindrom sayi kactir 
#polindrom sayilar iki taraftanda ayni okunur orngn = 9009

def check_3digits(x):
    str_x = str(x)
    if len(str_x) == 3:
        return x 
    
def is_carpan(y,x):
    if y % x == 0:
        return x 

carpanlar = [] 

for i in range(10000,998001):
    str_number = str(i)
    if str_number == str_number[::-1]:
        for j in range(100,1000):
            if is_carpan(i,j):
                for k in range(100,1000):
                    if j*k == i:
                       carpanlar.append(j)
                       carpanlar.append(k)

carpan1 = carpanlar[-1]
carpanlar.pop()
carpan2 = carpanlar[-1]
print(f"{carpan1} x {carpan2} = {carpan1*carpan2}")
                        
                
                