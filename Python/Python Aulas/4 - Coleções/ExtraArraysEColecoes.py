# Aula 77 a 78

# Arrays (python não tem suporte, mas as listas podem ser utilizadas no lugar)

carros = ['Ford', 'Volvo', 'Jeep']
print(carros)

x  = carros[0]
print(x)

carros[0] = 'Ferrari'
print(carros)

x = len(carros)
print(x)

print('\n\n')

carros = ['Ford', 'Volvo', 'Jeep']

for x in carros:
    print(x)

carros.append('Ferrari')
print(carros)

carros.pop(1)
print(carros)

carros.remove('Ford')
print(carros)
