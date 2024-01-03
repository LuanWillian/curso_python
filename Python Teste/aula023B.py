try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um poblema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Não e possivel dividir um numero pos zero')
except KeyError:
    print('O usuario preferio não informa os dados')
except Exception as erro:
    print(f'O poblema foi {erro.__class__}')
else:
    print(r)
finally:
    print('Volte sempre!')
