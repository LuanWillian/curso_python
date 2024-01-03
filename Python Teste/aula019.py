'''filme = {'titulo': 'Vikings', 'ano': 2013}
filme['Genero'] = 'Ação/Nordico'
del filme['titulo']
print(filme)'''

'''c = 0
carros = [{'Carro': 'BMW', 'Ano': 2002}, {'Carro': 'Mercedes', 'Ano': 2000}]
while c != len(carros):
    print(f'O carro {carros[c]["Carro"]} tem o ano {carros[c]["Ano"]}')
    c +=1'''

'''print(filme.keys())
print(filme.values())
print(filme.items())

for c in filme.keys():
    print(c)
for c in filme.values():
    print(c)
for k,v in filme.items():
    print(k,v)'''

carros = {}
todos = []
for c in range(0,2):
    carros['Marca'] = str(input('Digite a marca do carro: '))
    carros['Modelo'] = str(input('Digite o modelo do carro: '))
    todos.append(carros.copy())

'''for c in range(0,len(todos)):
    print(f'A marca {todos[c]["Marca"]} tem o modelo {todos[c]["Modelo"]}')'''
for c in todos:
    for k,v in c.items():
        print(f'O {k} e {v}')
print(todos)