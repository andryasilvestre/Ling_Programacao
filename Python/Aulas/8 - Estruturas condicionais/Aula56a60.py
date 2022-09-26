        # If, elif e else
        
# Igual a: a==b
# Diferente de: a != b
# Menor que> a < b
# Menor ou igual a: a <= b
# Maior que: a > b
# Maior ou igual a: a >= b

a = 33
b = 200

if b > a: 
    print('b é maior que a')
elif a == b:
    print('a é igual a b.')
else:
    print('b é menor que a.')
    
print('\n\n')


        # Short hand if 
a = 33
b = 200
        
if b > a: print('b é maior que a')

        # Short hand if else
        
print('a é maior que b') if a > b else print('b é maior que a')
print('A') if a > b else print('B') if b > a else print('=')
print('\n\n')


        # Operadores lógicos
        
a = 200
b = 33
c = 500

if a > b and c > a:
    print("A condição \"a > b e c > a\" é verdadeira")
if a > b or c > a:
    print("Pelo menos uma das condições é verdadeira")
    
print('\n\n')


   
        # Estruturas condicionais aninhadas
    
x = 11

if x > 10:
    print('x > 10')
    if x > 20:
        print('x > 20')
    else: 
        print('x < 20')
        
if x > 20:
    pass        # se isso for verdadeiro, nada é executado, mas também não gera erro no código.