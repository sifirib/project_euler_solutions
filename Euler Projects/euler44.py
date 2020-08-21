
def do_the_math(n):
    return n*(3*n-1)/2

def is_pentagonal(x):
    return ((1 + (1 + 24 * x) ** (1/2)) / 6).is_integer()       
    


for i in range(1,10000):
    number1 = do_the_math(i)
    for j in range(i-1, 0, -1):
        number2 = do_the_math(j)
        if is_pentagonal(number1 + number2):
            if is_pentagonal(number1 - number2):

                print(number1-number2)