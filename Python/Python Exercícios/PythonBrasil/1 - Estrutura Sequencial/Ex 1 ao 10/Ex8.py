# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

def salarioMes():
    valHora = input("Quanto você ganha por hora? ")
    hrsMes = input("Quantas horas você trabalha por mês? ")
    salario = round(float(valHora) * float(hrsMes), 2)
    
    print("O seu salário total mensal é R$ ", salario)
    
salarioMes()
    
