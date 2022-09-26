#   Percorrer um dicionário com loop

dict1 = {
    "Nome": 'Maggie',
    "Idade": 4,
    "Peso": 7.1,
    "Descrição": 'Lombinho'
}

# for x in dict1:
#     print(x)            # imprime os itens

# for x in dict1:
#     print(dict1[x])     # imprime os valores

for x in dict1.values():
    print(x)

for x in dict1.keys():
    print(x)
print("\n")

for x, y in dict1.items():  # chave/valor
    print(x + ':', y)
print("\n")

#   Copiar dicionários      -- dict2 = dict1 apenas faz uma atribuição, e não uma cópia.

dict2 = dict1.copy()
print(dict2)

dict3 = dict(dict1)
print(dict3)

#   Dicionários aninhados (que contém outros dicionários)

minhasFilhas = {
    "filha1": {
        "Nome": 'Maggie',
        "Idade": 4,
        "Apelido": 'Virgolini'
    },

    "filha2": {
        "Nome": 'Petunia',
        "Idade": 2,
        "Apelido": 'Tunia'

    }
}

filha1 = {
    "Nome": 'Maggie',
    "Idade": 4,
    "Apelido": 'Virgolini'
}

filha2 = {
    "Nome": 'Petunia',
    "Idade": 2,
    "Apelido": 'Tunia'
}

filhotas = {
    "filha1": filha1,
    "filha2": filha2
}

print(minhasFilhas)
print(filhotas)