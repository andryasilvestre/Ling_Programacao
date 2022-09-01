#   Copiar listas

lista = ['maçã', 'banana', 'pera', 'cereja', 'pera']

#   dois meios de copiar uma lista:
#outra = lista.copy()
outra = list(lista)
lista.append("jabuticaba")  # append vai a string completa. extend vai caractere por caractere

print(lista)
print(outra)
print('\n\n\n')

#################       Juntar listas  ---> 3 meios

lista1 = ['maçã', 'banana', 'pera', 'cereja', 'pera']
lista2 = [1, 3, 12, 5, 90]
#lista3 = lista1 + lista2

# for x in lista2:
#     lista1.append(x)

lista1.extend(lista2)

print("Lista 3:", lista1)

