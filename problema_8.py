t=list(map(int,input('Introduceti temperaturile măsurate din oră în oră pe parcursul a 24 de ore: ').split(',')))
print(f'a)temperatura medie este {sum(t)/24}')
print(f'b)maximul temperaturii este {max(t)}, iar minimul este {min(t)}')
print(f'c)ora (orele) la care s-a înregistrat temperatura maximă este ', end='')
for i in t:
    if i==max(t):
        print(t.index(i)+1)
print('c)ora (orele) la care s-a înregistrat temperatura minima este ', end='')
for i in t:
    if i==min(t):
        print(t.index(i)+1)
n1=0
print('e)numărul de zile în care au fost înregistrate temperaturi mai jos de zero grade este ', end='')
for i in t:
    if i<0:
        n1+=1
print(n1)
n2=0
print('f)numărul de zile în care au fost înregistrate temperaturi mai mari de media săptămânală este ', end='')
for i in t:
    if i>sum(t)/24:
        n2+=1
print(n2)