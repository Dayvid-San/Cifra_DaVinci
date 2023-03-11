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
            listFound.append(restor)
        
    # unir números do input aos números gerados

    
        resultado =''.join(listFound)
        print(resultado.split(','))


cifra()
