import os

os.system('cls') or None

def prod():
    num = input("Digite um número: ")    # INPUT retorna string e não um campo numérico
    num2 = input("Digite outro número: ")
    prodt = float(num) * float(num2)
    
    print("O produto de ", num, " X ", num2, " é igual à: ", prodt)
    
prod()