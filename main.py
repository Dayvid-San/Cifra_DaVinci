def cifra():
    num = int(input('Qual o número?\n'))
    res = []
    res.append(num)

    p = str(input('Vai adicionar outro número?\n'))
    if p == 'y':
        cifra()
    else:
        print('Este são os números: {}'.format(res))




cifra()