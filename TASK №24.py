#номер 26
a=open("k7a-6.txt").readline()
k=0
maxi=0
for i in a:
    if i!="E" and i!="A":
        k+=1
        maxi=max(k,maxi)
    else:
        k=0
print(maxi)
#ответ 20
# номер 27
a=open("k7b-1.txt").readline()
s=''
while s+"EAB" in a:
    s+='EAB'
if s+"E" in a:
    s+="E"
    if s+"A" in a:
            s+="A"
print(len(s))
#ответ 7
# номер 37
a = open("k7c-5.txt").readline()
k = 1
h = 0
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        k += 1
    else:
        k = 1
    if k >= 5:
        h += 1
print(h)
#ответ 4904
# номер 53
a = open("k8-4.txt").readline()
Z=a[0]
k=1
maxi=1
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        k+=1
        if k>maxi:
            maxi=k
            Z=a[i]
    else:
        k=1
print(Z,maxi)
#ответ W 4
# номер 77
a = open("k8-1.txt").readline()
k=1
maxi=1
for i in range(len(a)-1):
    if a[i]!=a[i+1]:
        k+=1
        if k>maxi:
            maxi=k
    else:
        k=1
print(maxi)
#овтвет 159
# номер 87
a = open("24-1.txt").readline()
C="QWERTYUIOPASDFGHJKLZXCVBNM"
S="1234567890"
F=''
for i in range(len(a)-1):
    if a[i] in S:
        F+=a[i]
    if a[i] in S and a[i+1] in C:
        F+=" "
print(F)
#ответ 7642289
# номер 93
a = open("24.txt").readline()
k=1
maxi=0
for i in range(len(a)-1):
    if a[i]<a[i+1]:
        k+=1
    else:
        maxi=max(k,maxi)
        k=1
print(maxi)
#ответ 3
# номер 137
a = open("24-s1.txt").readlines()
k=0
for i in a:
    if i.count("J")>i.count("E"):
        k+=1
print(k)
#ответ 482
# номер 141
a = open("24-s1.txt").readlines()
k = 0
for line in a:
    for i in range(len(line) - 2):
        if line[i] == "F" and line[i + 2] == "O":
            k += 1
            break  
print(k)
#ответ 757
