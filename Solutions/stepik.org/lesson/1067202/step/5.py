a1, a2, a3, a4 = input().split()
a1, a2, a3, a4 = int(a1), int(a2), int(a3), int(a4)
l=[]
if a2<0:
    a2-=1
elif a2>0:
    a2+=1

for i in range(a1,a2,a3):
    l+=[i]
if a4!=0:
    for i in l:
        if (l.index(i)+1)%a4==0:
            l.remove(i)
print(l)
