masculino = 'M'.upper()
feminino = 'F'.upper()
sexo = ''
while not sexo == masculino and not sexo == feminino :
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if sexo != masculino and sexo != feminino:
        print('Ops, parece que voce digitou errado! tente novamente!')
print('Sexo {} cadastrado com sucesso!'.format(sexo))