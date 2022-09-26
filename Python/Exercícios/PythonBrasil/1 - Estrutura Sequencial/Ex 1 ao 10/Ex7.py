# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def areaQ():
    base = input("Digite a base do quadrado: ")
    area = float(base) ** 2
    areaDobro = 2 * round(area, 2)
    
    print("O dobro da área do quadrado é:", areaDobro)

areaQ()