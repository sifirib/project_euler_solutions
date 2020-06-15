#1 den 20 ye kadar olan sayilarin hepsine bolunebilen en kucuk sayi kactir

#cozum1(BRUTEFORCE ATTIM)

list = []
i = 1
k = 0
while True:
   
    
    for j in range(1,21):
        if i % j == 0:
            k += 1
            if k == 20:
                print(i)
    i += 1
    k = 0


#cozum2

import math 

liste = []

for i in range (1,21):
    liste.append(i)

def gcd(x,y):
    return math.gcd(x,y)

def lcm(x,y):
    return (x*y) // gcd(x,y)

while True:
    n = 0
    j = lcm(liste[n],liste[n+1])
    del liste[0:2]
    liste.insert(0,j)
    if len(liste) == 1:
        print(liste[0])
    
    



















