#binden kucuk olup 3 veya 5 e tam bolunen 
#sayilarin toplami kactir
toplam = 0
for sayi in range(1,1000):
    if sayi % 3 == 0 or sayi % 5 == 0:
        toplam += sayi
        
print(toplam)


