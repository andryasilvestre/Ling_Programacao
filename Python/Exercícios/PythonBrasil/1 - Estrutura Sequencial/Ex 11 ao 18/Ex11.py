# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#           a - o produto do dobro do primeiro com metade do segundo .
#           b - a soma do triplo do primeiro com o terceiro.
#           c - o terceiro elevado ao cubo.

int1 = int(input("Digite um número inteiro: "))
int2 = int(input("Digite outro número inteiro: "))
real1 = float(input("Digite um número real: "))

def produto(int1, int2, real1):
    prod = (2 * int1) * (0.5 * int2)
    print("Produto =", round((prod),2))
    
def soma(int1, int2, real1):
    somaT = round(((3 * int1) + real1), 2)
    print("Soma = ", somaT)
    
def tercCubo(int1, int2, real1):
    cubo = round((real1**3),5)
    print("Cubo do númreo real =", cubo)
    
print("\n")    
produto(int1, int2, real1)
soma(int1, int2, real1)
tercCubo(int1, int2, real1)