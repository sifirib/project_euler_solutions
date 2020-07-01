from itertools import permutations 

numbers = "0123456789"
perms = list(permutations(numbers))
answer = perms[999999]
answer2 = "".join(answer)

print(answer2)
