def spisok(arg):
    a1, a2, a3, a4 = arg.split()
    a1, a2, a3, a4 = int(a1), int(a2), int(a3), int(a4)
    l = []
    it = 0
    if a2 < 0:
        a2 -= 1
    elif a2 > 0:
        a2 += 1

    for i in range(a1, a2, a3):
        it+=1
        if a4==0:
            l+=[i]
        elif it%a4!=0:
            l += [i]

    return l