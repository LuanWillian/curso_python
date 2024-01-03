'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Luan'
teste[1] = 16
galera.append(teste[:])
print(galera)'''

'''galera = [['João', 19],['Ana', 33],['Joaquim', 13],['Maria', 25]]
for c in galera:
    if c[1] > 18:
        print(c)'''

galera = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()
print(galera)