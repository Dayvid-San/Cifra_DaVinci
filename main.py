def leitor(lista, aux = 0):
    if lista == []:
        return lista
    else:
        aux += 1
        leitor(lista[aux], aux)


def cifra(lista = []):
    num = int(input('Qual o número?\n'))
    lista.append(num)

    p = str(input('Vai adicionar outro número?\n'))
    if p == 'y':
        cifra()
    else:
        aux = 0
        listFound = []

        for i in lista:
            restor = i * '{}'.format(aux)
            aux += 1
            return listFound.append(restor)

        print('Este são os números: {}'.format(listFound))


cifra()
