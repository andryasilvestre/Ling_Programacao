# Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#                   a - Para homens: (72.7*h) - 58
#                   b - Para mulheres: (62.1*h) - 44.7

def pesoIdeal():
    altura = float(input("Informe a sua altura: "))
    pesoIdealH = round(((72.7*altura) - 58),2)
    pesoIdealM = round(((62.1*altura) - 58),2)
    
    print("Peso ideal homem:", pesoIdealH)
    print("Peso ideal mulher:", pesoIdealM)
    
pesoIdeal()