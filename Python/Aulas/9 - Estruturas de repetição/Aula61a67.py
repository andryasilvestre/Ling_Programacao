        # Loop de repetição while
        
i = 1
while i < 6:
    print(i) 
    i += 1
else:
    print('i é maior que 6')
    
print('Fim do programa.')

        # Loop de repetição for
        
nomes = ['Maggie', 'Freddie', 'Petunia']

for i in nomes:
    print(i)
else:
    print('Fim')
    
for i in 'M a g g i e':
    print(i)

print('\n\n')


    
        # Função range

for i in range(6):
    print(i)
    
for i in range(2,6):
    print(i)
    
print('\n\n')

for i in range(2, 12, 4):
    print(i)

        # Instrução break

i = 1 
while i < 6:
    print(i)
    if (i == 3):
        break
    i += 1

nomes = ['Maggie', 'Freddie', 'Petunia']
for i in nomes:
    print(i)
    if (i == 'Freddie'):
        break
    
print('\n\n')


        # Instrução continue


i = 0
while i < 6:
    i += 1
    if (i==3):
        continue
    print(i) 


nomes = ['Maggie', 'Freddie', 'Petunia']
for i in nomes:
    if (i == 'Freddie'):
        continue
    print(i)
    
    
        # Loops aninhados 
        
nomes = ['Maggie', 'Freddie', 'Petunia']
sobrenomes = ['Silvestre', 'May']

for x in nomes:
    for y in sobrenomes:
        x = x + ' ' + y
    print(x)


        # Declaração de passagem nos loops
        
print('\n inicio')

for x in [0, 3, 4]:
    pass

print('\n inicio')
