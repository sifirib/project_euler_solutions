#600851475143 sayisinin en buyuk asal carpani nedir


def prime_check(x):
    prime = True
    
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            prime = False
            continue
    return prime


number = 600851475143

for i in range(2,int(number**0.5)+1):
    if number % i == 0 and prime_check(i):
        sonuc = i
        
print(sonuc)
         
        



            
        