lista = ['maçã', 'banana', 'pera', 'cereja', 'pera']
lista[1] = 'abacaxi'

print(lista)

lista[1:3] = ['jujuba', 'macaiba', 'pera', 'abacate']
print(lista)
lista[1:5] = ['abacate']
print(lista, '\n\n')

lista.insert(2, 'teste')    #   não altera os itens existentes na lista.

print(lista)

#   Adicionar itens na lista

lista.append("sucrilhos")   #   adiciona no final da lista
lista.insert(1, "cereal")
lista.extend(['teste2', 'teste3'])  #   adiciona no final da lista qualquer coisa, até mesmo outra lista.

outraLista = ['1', '2']
lista.extend(outraLista)
print(lista)

print('\n\n')

#   Remover itens da lista

lista.remove('teste')   #   tem que especificar o elemento a ser removido
print(lista)

lista.pop(1)    # tem que especificar o número, a nao ser que seja o ultimo item: lista.pop()
print(lista)

del lista[1]
print(lista)

lista.clear()
print(lista)

