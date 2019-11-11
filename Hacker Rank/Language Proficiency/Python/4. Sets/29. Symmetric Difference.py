m = int(input())
mSet = set(input().split())
n = int(input())
nSet = set(input().split())
symDif = mSet ^ nSet
sortedSymDif = sorted(list(symDif), key=int)
print('\n'.join(sortedSymDif))
