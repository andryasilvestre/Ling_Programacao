# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def media():
    n1 = input("Digite a primeira nota: ")
    n2 = input("Digite a segunda nota: ")
    n3 = input("Digite a terceira nota: ")
    n4 = input("Digite a quarta nota: ")
    
    med = (float(n1) + float(n2) + float(n3) + float(n4))/4
    
    print("A média das notas é: ", med)
    
media()