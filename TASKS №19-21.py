#m=1(1 й ход Пети в игре)
#m=2(1 й ход Вани в игре)
#m=3(2 й ход Пети в игре)
#m=4(2 й ход Пети в игре)


def f(s,m):
    if s>=301: return m%2==0#улсовие для победы
    if m ==0:return 0#условие для проигрыша
    g=[f(s+3,m-1),f(s*5,m-1)]
    return any(g) if (m-1)%2==0 else all(g)
print("19",[s for s in range(1,301) if not f(s,1) and f(s,2)])
print("20",[s for s in range(1,301) if not f(s,1) and f(s,3)])