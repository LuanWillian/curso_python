def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


i = int(input('numero: '))
print(par(i))