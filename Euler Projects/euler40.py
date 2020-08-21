i = 1
stri = ''
while len(stri) < 1000001:
    stri += str(i)
    i += 1
answer = int(stri[0]) * int(stri[9]) * int(stri[99]) * int(stri[999]) * int(stri[9999]) * int(stri[99999]) * int(stri[999999])
print(answer)
