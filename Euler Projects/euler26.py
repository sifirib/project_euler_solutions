max_devir = 0
bolen = 2

while bolen < 1000:
    kalanlar = []
    bolunen = 1
    while True:
        kalan = bolunen % bolen
        if kalan in kalanlar:
            ilk_index = kalanlar.index(kalan)
            son_index = len(kalanlar)
            if son_index - ilk_index > max_devir:
                max_devir = son_index - ilk_index 
                theanswer = bolen
            break
        bolunen = 10 * kalan
        kalanlar.append(kalan)
				
    bolen += 1	

print(theanswer)
	
