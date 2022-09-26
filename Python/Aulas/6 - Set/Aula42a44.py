# Coleção não ordenada, não pode ser alterada e não permite duplicatas..

set1 = {'Maggie', 'Petunia', 'Freddie', 'Maggie'}
print(set1)
print(len(set1))

set2 = {'Maggie', 8, True}
set3 = {1, 2, 3, 4, 5}
set4 = {True, False, False}

print(type(set2))

set5 = set(('Maggie', 'Petunia'))
print(set5)

# Acessando os itens do set -- como não é ordenado, não pode ir pelo indice ou chave

for i in set1:
    print(i)

print('Maggie' in set1)

# Add novos itens no set

set1.add('Frederico')
print(set1)

# set22 = {'Nick', 'Lion', 'Focalicia'} --- set também itera com lista
set22 = ['Nick', 'Lion', 'Focalicia']

set1.update(set22)

print(set1)