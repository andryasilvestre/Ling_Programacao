# Passando uma lista como argumento

def funcao(alimentos):
    for x in alimentos:
        print(x)
        
frutas = ['Abacaxi', 'Abacate', 'Maçã', 'Pera', 'Uva', 'Morango', 'Caju', 'Cajá']

funcao(frutas)
funcao(['Peixe', 'Carne'])

print('\n\n')

# Declaração de passagem nas funções

def funct():
    pass

funct()
print('Fim do programa')
print('\n\n')


# Recursividade das funções

    # sem recursividade
def repetir(n):
    for x in range(n):
        print('Olá mundo!')
        
repetir(4)

    # com recursividade
def repetirRecursivo(n):
    if (n > 0):
        print('Olá mundo!')
        repetirRecursivo(n - 1)
    
repetirRecursivo(5)


# Funções LAMBDA

x = lambda a : a + 10
print(x(5))

# resultado = x(5)
# print(resultado)

x = lambda a, b : a * b
print(x(2, 5))

def myFunc(n):
    return lambda a : a * n

meuDuplicador = myFunc(2)
print(meuDuplicador(11))

triplicador = myFunc(3)
print(triplicador(3))

print('\n\n')

# Entrada de dados do usuário -- 3.6 ++ = input() // 2.7 = raw_input()

user = input('Digite o seu nome: ')
print('Seja bem-vindo, ' + user)