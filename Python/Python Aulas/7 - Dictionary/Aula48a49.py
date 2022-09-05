#   Intro. a dicionário e como acessar os itens

dict1 = {  
    "Nome": 'Maggie', 
    "Idade": 4, 
    "Peso":7.1, 
    "Descrição": 'Lombinho'
}

print(dict1["Nome"])
print(dict1["Descrição"])

x = dict1.get("Idade")
print(dict1.get("Idade"))   # print(x)

x = dict1.keys()    # retorna uma lista com todas as chaves do dicionário
print(x)

# dict1.keys reflete a lista original das chaves; portanto ele mostra quando elas forem alteradas.

dict1["Raça"] = 'Shih-Tzu'
print(x)

x = dict1.values()
print(x)

x = dict1.items()    #imprime a tupla da lista de itens. ** ao att um valor, a tupla também atualiza **
print(x)

if "Idade" in dict1:
    print("Sim. Idade é uma das chaves desse dicionário.")