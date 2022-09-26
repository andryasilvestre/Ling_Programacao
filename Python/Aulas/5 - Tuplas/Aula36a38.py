######### Tupla é uma coleção ordenada e imutável (diferente das listas).

tupla = ('Maggie', 'Petunia', 'Freddie', 'Maggie')
print(tupla)
# tam = len(tupla)
# print(tam)
print(len(tupla))

tupla2 = ('carro')  # não é uma tupla. É uma string.
tupla3 = ('carro',) # precisa da vírgula quando tem 1 campo para ser reconhecido como tupla.

print(type(tupla2))
print(type(tupla3))

tupla4 = (1,2,3,4)
tupla5 = (True, False, True, True)
tupla6 = ('Gabriel', 1, 1.50, True)

print(type(tupla6))

tupla7 = tuple(('Maçã', 'Banana', 1, 1.5, True))    # utilizando o construtor tuple()
print(type(tupla7))

# print('Gabriel' in tupla6)  #   imprime True ou False

# if 'Gabriel' in tupla6:
#     print('Sim, contém.')
# else:
#     print('Não, não contém.')
    
# if 'a' in tupla6:
#     print('Sim, contém.')
# else:
#     print('Não, não contém.')

print('\n\n')


#   Atualizar tuplas

x = ('Maggie', 'Petunia', 'Freddie', 'Maggie')
print(x)

y = list(x)
y[2] = 'Petunia'
y.append('Maggie')
print(y)

x = tuple(y)
print(x)
print('\n')

        #   Não se pode alterar uma tupla, mas pode adicionar ela a outra tupla
x = ('Maggie', 'Petunia', 'Freddie', 'Maggie')
y = ('Fredericksen',)
x+=y

y = list(x)
y.remove('Freddie')
x = tuple(y)

#del x   # Dá erro. Diz que ' x ' não existe, pois x foi removido com       ' del x '
print(x)