# BUSCA
""" Retorna o indice elem se esle estiver na lista ou None, caso contrário """
def busca(lista, elem):
    for i in range(len(lista)):
        if lista == elem:
            return i
        return None

lista_estranha = [8, "5", 32, 0, "python", 11]
elemento = 0

indice = busca(lista_estranha, elemento)

if indice is not None:
    print(f"indice = {indice}")
else: 
    print("Elemento não encontrado!")

# INSERÇÃO
def insercao(lista, elemento, indice):
    lista_nova = lista[:indice:] + [elemento] + lista[indice:]
    return lista_nova

listaI = [1,2,3,4,5,6,7,8]
elementoI = 9
indiceI = 2
listaI = insercao(listaI, elementoI, indiceI)
print(listaI)


# REMOÇÃO
def remocao(lista, indice):
    elemento = lista[indice]
    lista_nova = lista[:indice] + lista[indice + 1:]
    return lista_nova

listaR = [1,2,3,4,5,6,7,8]
indiceR = 0
listaR = remocao(listaR, indiceR)
print(listaR)
 
