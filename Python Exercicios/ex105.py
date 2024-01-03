def notas(*n, situa=False):
    """
        Calcula a media da turma e coloca em um dicionario.
    :param n: Pega uma lista com varios valores dentro.
    :param situa: Da a opção de colocar ou não a situação da turma
    no dicionario.
    :return: Retorna um dicionario.
    """
    maior = 0
    menor = 0
    soma = 0
    media = 0
    notasAluno = {}
    for c in n:
        compri = len(c)
        for d in range(0, compri):
            if d == 0:
                maior = c[d]
                menor = c[d]
            else:
                if maior < c[d]:
                    maior = c[d]
                if menor > c[d]:
                    menor = c[d]
        for i in c:
            soma += i
        media = soma / compri
    notasAluno['Total'] = compri
    notasAluno['Maior'] = maior
    notasAluno['Menor'] = menor
    notasAluno['Media'] = media

    if situa:
        if media == 7.0:
            notasAluno['Situação'] = 'Ta na media'
        if media > 7.0:
            notasAluno['Situação'] = 'Ta muito boa'
        if media < 7.0:
            notasAluno['Situação'] = 'Ta muito ruim'
    return notasAluno


lista = []
while True:
    valor = float(input('Nota do aluno: '))
    lista.append(valor)
    usuario = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if usuario == 'N':
        break
print(notas(lista, situa=True))
help(notas)
