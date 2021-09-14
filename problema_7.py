v = list(map(int,input('Introduceti venitul zilnic al unei saptamani: ').split(',')))
print(f'a)venitul săptămânal al întreprinderii este {sum(v)}')
print(f'b)media venitului zilnic este {sum(v)/7}')
print(f'c)ziua în care s-a obţinut cel mai mare venit este ', end='')
if v.index(max(v))==0: 
    print('luni')
elif v.index(max(v))==1: 
    print('marti')
elif v.index(max(v))==2: 
    print('miercuri')
elif v.index(max(v))==3: 
    print('joi')
elif v.index(max(v))==4: 
    print('vineri')
elif v.index(max(v))==5: 
    print('sambata')
else:
    print('duminica')
print('d)ziua cu venitul cel mai mic este ', end='')
if v.index(min(v))==0: 
    print('luni')
elif v.index(min(v))==1: 
    print('marti')
elif v.index(min(v))==2: 
    print('miercuri')
elif v.index(min(v))==3: 
    print('joi')
elif v.index(min(v))==4: 
    print('vineri')
elif v.index(min(v))==5: 
    print('sambata')
else:
    print('duminica')