#a<b<c ve a^2 + b^2 = c^2 ve a+b+c = 1000     a.b.c sayisi nedir?

#cozum1 (bruteforce)
for a in range(1,1000):
    for b in range(1,1000 - a):
        c = 1000 - a - b
        
        if a**2 + b**2 == c**2:
            if a<b<c:
                print(a*b*c)
        
#cozum2
                
