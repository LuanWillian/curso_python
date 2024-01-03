print('-'*40)
print('         LISTAGEM DE PREÇOS')
print('-'*40)
listagem = ('Lapis','1,75','Borracha','2,00','Caderno','15,90','Estojo','25,00','Transferidor','4,28','Compasso','9,99',
'Mochila','120,32','Canetas','22,38','Livro','34,90')

'''print(f'{listagem[0]}........................R$  {listagem[1]}')
print(f'{listagem[2]}.....................R$  {listagem[3]}')
print(f'{listagem[4]}......................R$  {listagem[5]}')
print(f'{listagem[6]}.......................R$  {listagem[7]}')
print(f'{listagem[8]}.................R$  {listagem[9]}')
print(f'{listagem[10]}.....................R$  {listagem[11]}')
print(f'{listagem[12]}......................R$  {listagem[13]}')
print(f'{listagem[14]}......................R$  {listagem[15]}')
print(f'{listagem[16]}........................R$  {listagem[17]}')'''

for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}',end='')
    else:
        print(f'R${listagem[c]:>8}')
print('-'*40)