#1
from itertools import *
s="38 58 146 36 27 347 568 127".split()  #сколько совпадений между строкой и столбоцом(номер столбца)
v="DE EA AH HC CF FG GH GB BE BD".split()  #название всех дорог
print(*range(1,9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b)+1) in s[p.index(a)] for a,b  in v):
        print(*p)
#ответ 31
#2
print('x','y','z','w','F',sep='\t')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f= ((not w) and x and y and (not z))or((not w) and x and y and z)or ((not w) and x and (not y) and (not z))
                if f==1:
                    print(x,y,z,w,bool(f),sep='\t')
#yzxw
#4-18
#5
for N in range(1,500):
    R=bin(N)[2:]
    sumi=R.count('1')
    deli=sumi%3
    D=bin(deli)[2:]
    R=R+D
    sumi_2=R.count('1')
    deli_2=sumi_2%2
    R=R+str(deli_2)
    R=int(R,2)
    if R>116:
        print(N)
#ответ 17
#6-60
#7-86
#8
k=0
for i1 in range(1,13):
    for i2 in range(1,13):
        for i3 in range(1,13):
            for i4 in range(1,13):
                for i5 in range(1,13):
                    num=i1*12**4+i2*12**3+i3*12**2+i4*12+i5
                    s=str(num)
                    if s.count("3")==1 and (s.count("10")+s.count("11"))>2:
                        k+=1
print(k)
# ответ 8
#11 - 110
#13-24
