casa = float(input('Digite o valor da casa R$: '))
salario = float(input('Digite o seu salario R$:'))
ano = float(input('Digite quantos anos voce quer pagar: '))
minimo = salario * 30/100
boleto = casa / (ano * 12)

if boleto <= minimo:
    print('Seu credido foi APROVADO!')

else:
    print('Seu credito foi NEGADO!')
