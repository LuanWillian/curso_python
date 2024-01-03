def test(b):
    global a
    a = 10
    b += 4
    c = 1
    print(a)
    print(b)
    print(c)


a = 5
test(a)
print(f'A fora vale {a}')
