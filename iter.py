import itertools
data=input("enter characters:")
permute=list(itertools.permutations(data))
print("all permutations")
for p in permute:
    print(' '.join(p))
    