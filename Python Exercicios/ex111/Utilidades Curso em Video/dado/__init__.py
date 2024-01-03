def leiaDinhero(msg):
    while True:
        preco = str(input(msg)).strip()
        g = preco
        preco = preco.replace(',', '')
        preco = preco.replace('.', '')
        if preco.isnumeric():
            g = g.replace(',', '.')
            f = float(g)
            return f
        else:
            print(f'Erro! {preco} e um preço invalido!')