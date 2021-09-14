x = list(map(int,input('Introduceti cinci numere: ').split(',')))
y=x
print(f'a) suma primelor trei componente ale variabilei x este {sum(x[0:3])}')
print(f'b) suma tuturor componentelor variabilei y este {sum(y)}')
p=1
for i in range(0,len(x)):
    p*=x[i]
    i+=1
print(f'c) produsul tuturor componentelor variabilei x este {p}')
print(f'd) valoarea absolută a componentei a treia a variabilei y este {abs(x[2])}')
print(f'e) suma primelor componente ale variabilelor x şi y este {x[0]+y[0]}')