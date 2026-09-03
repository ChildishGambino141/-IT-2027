from itertools import *
s="256 13 245 356 134 14".split()  #сколько совпадений между строкой и столбоцом(номер столбца)
v="FC CB BE EA AF FD DB DE".split()  #название всех дорог
print(*range(1,7))
for p in permutations('ABCDEF'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b  in v):
        print(*p)