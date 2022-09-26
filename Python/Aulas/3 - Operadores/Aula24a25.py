# Operadores de identidade

x = ['Apple', 'Banana']
y = ['Apple', 'Banana']
z = x

print (x is z)
print (x is y)
print(x == y)       # em conteúdo

print("\n")

print (x is not z)
print (x is not y)
print(x != y)

print("\n\n")

#Operadores de associação

x = ['Maçã', 'Banana']

print('Banana' in x)
print('banana' in x)

print('Banana' not in x)

x = [30, 40, 60]
print(34 in x)
print(30 in x)