counter = 1
for pound in range(0,3):
    if pound*100 > 200:
        break
    for ellip in range(0,5):
        if pound*100 + ellip*50 > 200:
            break
        for yirmip in range(0,11):
            if pound*100 + ellip*50 + yirmip*20 > 200:
                break
            for onp in range(0,21):
                if pound*100 + ellip*50 + yirmip*20 + onp*10 > 200:
                    break
                for besp in range(0,41):
                    if pound*100 + ellip*50 + yirmip*20 + onp*10 + besp*5 > 200:
                        break
                    for ikip in range(0,101):
                        if pound*100 + ellip*50 + yirmip*20 + onp*10 + besp*5 + ikip*2 <= 200:
                            counter += 1
                            
                                
print(counter)                                