# Alterar, adicionar e remover itens de um dicionário

    # Alterar
    
dict1 = {  
    "Nome": 'Maggie', 
    "Idade": 4, 
    "Peso":7.1, 
    "Descrição": 'Lombinho'
}

dict1['Nome'] = "Melgs"
print(dict1)

dict1.update({"Idade": 4.2})
print(dict1)


    #   Adicionar

dict1["Raça"] = 'Shih-Tzu'
print(dict1)

dict1.update({"Cor": 'Preto e branco'})
print(dict1)


    #   Remover

dict1.pop("Cor")
dict1.popitem()     #   Remove o último item (nesse caso, raça)
del dict1["Idade"]
    # dict1 => remove o dicionário inteiro da memória.
    
dict1.clear()   #   Remove o conteúdo do dicionário, mas ele ainda existe na memória.
    
print(dict1)
