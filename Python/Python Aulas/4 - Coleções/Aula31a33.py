#   Iterando listas com loop.

lista = ['maçã', 'banana', 'pera', 'cereja', 'pera']

#for x in lista:
#    print(x)

#for i in range(len(lista)):
#    print(lista[i])

'''
i = 0
while (i < 5):
    print(lista[i])
    i = i + 1
'''

[print(x) for x in lista]
    
print("Fim da execução.")

print('\n\n')               # obs - ctrl + ; ---- comenta várias linhas ao mesmo tempo


# Compreensão de listas

lista = ['maçã', 'banana', 'pera', 'cereja', 'pera']
novaLista = []

# for x in lista:
#     if "r" in x:            #qual nome contem a letra 'r'
#         novaLista.append(x)
        
# print(novaLista)

# novaLista = [x for x in lista if "r" in x]
#novaLista = [x for x in lista if x != 'pera']
novaLista = [x for x in lista]
novaLista = [x for x in range(10) if x % 2 == 0]
novaLista = [x.capitalize() for x in lista] #   .upper() ou .lower()
novaLista = ["Olá" for x in lista]

novaLista = [x if x != 'pera' else 'Pera' for x in lista] 


print(novaLista)
print('\n\n')


# Classificação de listas

lista = ['maçã', 'banana', 'Pera', 'cereja', 'pera']    #upper vem antes de lower
listaN = [50, 100, 200, 32, 12, 23]

lista.sort(reverse = True)  #   na ordem reversa da *posição* (usar reverse)
listaN.sort()

# def myfunction(n):  
#     return abs(n - 50)    #n - 50 é do mais perto do 50 para ' - '. se for para +, entao n + 50

# listaN.sort(key = myfunction)   #   imprime com base no número mais próximo do 50.

lista.sort(key = str.lower) #   não distingue por letras maiusculas e minusculas.

lista.reverse()
listaN.reverse()

print(lista)
print(listaN)
