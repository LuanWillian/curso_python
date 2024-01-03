from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
dados['Idade'] = idade
dados['CTPS'] = int(input('Carteira de trabalho (0 SE NÃO TIVER): '))
if dados['CTPS'] == 0:
    print('*'*50)
    print()
    for k,v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salario'] = float(input('Salario R$'))
    dados['Aposentadoria'] = dados['Contratação'] - ano + 35
    print('*'*50)
    print()
    for k,v in dados.items():
        print(f'{k} tem o valor {v}')
