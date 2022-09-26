#   Descompactando tuplas

nomes = ('Maggie', 'Petunia', 'Freddie', 'Maggie')
print(nomes, '\n')

#(nome1, nome2, nome3, nome4) = nomes
#(nome1, nome2, *nome3) = nomes      

                                  # a variável marcada com * ---> atribui o restante dos nomes a uma lista:
(nome1, *nome2, nome3) = nomes  
print(nome1)
print(nome2)
print(nome3)

print('\n\n')

nomes = ('Maggie', 'Petunia', 'Freddie', 'Maggie')

# for x in nomes:
#     print(x)

# for i in range(len(nomes)):
#     print(nomes[i])

i = 0
while i < len(nomes):
     print(nomes[i])
     i+=1
     
print('\n\n')

nomes = ('Maggie', 'Petunia', 'Freddie')
nomes2 = (1, 3, 6, 8)
nomes3 = nomes + nomes2 
nomes4 = nomes2 * 2

print(nomes4)