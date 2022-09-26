        #   Funções

def funcao():
    print('Olá da função')
    
def cumprimenta(nome):
    print('Olá,', nome)
    
def multiplica(x):
    return x * 5
    

funcao()
cumprimenta("Ândrya")

print(multiplica(3))
result = multiplica(4)
print(result)
print('\n\n')


        #   Parametros das funções
    
def nomeCompleto(nome, sobrenome):
    print(nome + ' ' + sobrenome)
    print(nome, sobrenome)

nomeCompleto('Maggie', 'May')
print('\n\n')

def listaNomes(*nomes):      # * no *nome cria uma tupla no parametro
    for x in nomes:
        print(x)

def listaNomes2(*nomes):
    print(nomes)

listaNomes("Maggie", "Freddie", "Petunia", 'Tunia')
listaNomes2("Maggie", "Freddie", "Petunia", 'Tunia')