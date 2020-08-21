def is_pentagonal(x):
    return ((1 + (1 + 24 * x) ** 0.5)/ 6).is_integer() 

def is_triangular(x):
    return ((-1 + (1 + 8 * x) ** 0.5) / 2).is_integer()
    
def is_hexagonal(x):
    return ((1 + (1 + 8 * x) ** 0.5) / 4).is_integer()

n = 144
while True:    
    hex_number = n * (2 * n - 1)
    if is_triangular(hex_number) and is_pentagonal(hex_number):
        print(hex_number)
        break
    n += 1
        