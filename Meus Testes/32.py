for c in range(0,1):
    n = str(input('nome: '))
    i = str(input('indade: '))
    aa = open('dd1', 'a')
    aa.write(f'{n}\n{i}')

dados1 = open('dd1', 'r')
l = list()
b = list()
cc = 0
for c in dados1:
    if cc % 2 == 0:
        l.append(c.replace('\n', ''))
    else:
        l.append(c[:2])
        b.append(l.copy())
        l.clear()
    cc +=1

for c in range(0, len(b)):
    print(f'{b[c][0]}          \t{b[c][1]} anos')