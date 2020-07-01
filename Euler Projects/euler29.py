
terms = []
for a in range(2,101):
    for b in range(2,101):
        number = a ** b
        
        if number in terms:
            continue
        else:
            terms.append(number)

print(len(terms))
            