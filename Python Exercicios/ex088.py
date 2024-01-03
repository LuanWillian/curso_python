from time import sleep
from random import randint
lista = []
juncao = []
contador = 0
jogador = int(input('Jogos voce quer que eu sorteie: '))

for c in range(0, jogador):
    for d in range(0, 6):
        for e in range(0, 1):
            numero = randint(0, 60)
            if numero in juncao:
                while numero in juncao:
                    numero = randint(0, 60)
                juncao.append(numero)
            else:
                juncao.append(numero)
            if d == 5:
                lista.append(juncao[:])
                juncao.clear()

for c in range(0, len(lista)):
    lista[c].sort()
    contador += 1
    print(f'Jogo {contador}: {lista[c]}')
    sleep(1)
