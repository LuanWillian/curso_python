a = input('Digite algo: ')
print('Qual e o tipo primitivo {}'.format(type(a)))
print('So tem espaços? {}'.format(a.isspace()))
print('E um numero? {}'.format(a.isnumeric()))
print('E alfabetico? {}'.format(a.isalpha()))
print('E alfanumerico? {}'.format(a.isalnum()))
print('Esta em maisculas? {}'.format(a.isupper()))
print('Esta em minusculas? {}'.format(a.islower()))
print('Esta capitalizada? {}'.format(a.istitle()))