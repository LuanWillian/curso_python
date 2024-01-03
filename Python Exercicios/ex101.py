def voto(ano):
    """
    Essa função faz a validação de que uma pessoa pode ou não vota
    paran: Ano de nascimento
    retur: Retorna uma string se a pessoa pode vota ou não
    """
    from datetime import date
    idade = date.today().year - ano
    if idade < 18:
        return f'Com {idade} anos: VOTO NEGADO  '
    elif idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATORIO'
    elif idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL'


pessoa = int(input('Digite seu ano de nascimento: '))
print(voto(pessoa))
