# Remover itens do set

set1 = {'Maggie', 'Petunia', 'Freddie', 'Melgs'}
# set1.remove('Freddie')
set1.discard('Freddie')     # caso não encontre o item, ele continua o código sem gerar erros.

x = set1.pop()  #remove o ''ultimo'' item, mas o set não é ordenado, então...
print(x)
print(set1)

# set1.clear()
# print(set1)

# del set1
# print(set1)

# Loop através de um set

for x in set1:
    print(x)