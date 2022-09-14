# Argumentos de palavras-chave

def nomes(primeiro, segundo, terceiro):
    print('O primeiro nome é:', primeiro)
    print('O segundo nome é:', segundo)
    print('O terceiro nome é:', terceiro)

nomes(terceiro='Freddie', primeiro='Maggie', segundo='Petunia')

def nomeCompleto(**nome):   # ** -> não sabemos quantos são os valores de entrada // definimos como dictionary
    print(nome)
    for x in nome.values():
        print(x)
        
nomeCompleto(pri = 'Maggie', seg = 'Petunia', terc = 'Tunica', qua = 'Fred')
print('\n\n')


# Valor padrão de argumento

# def funcao(pais):
#     print('Eu sou de ' + pais)

# funcao()      --- da erro, pois é esperado um argumento

def funcao(pais = 'Brasil'):
    print('Eu sou do ' + pais)

funcao()
funcao('Uruguai')
funcao('Canadá')


