# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são 
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
#               a - salário bruto.                  
#               b - quanto pagou ao INSS.
#               c - quanto pagou ao sindicato.
#               d - o salário líquido.
#               e - calcule os descontos e o salário líquido, conforme a tabela abaixo:

def salarioMes():
    valHora = input("Quanto você ganha por hora? ")
    hrsMes = input("Quantas horas você trabalha por mês? ")
    salario = round(float(valHora) * float(hrsMes), 2)
    impRenda = round((salario * 0.11),2)
    inss = round((salario*0.08),2)
    sindicato = round((salario * 0.05),2)
    
    
    print( "\n" + "+ Salário Bruto : R$", salario)
    print("- IR (11%) : R$", impRenda)
    print("- INSS (8%) : R$", inss)
    print("- Sindicato ( 5%) : R$", sindicato)
    print("= Salário Liquido : R$", (salario - impRenda - inss - sindicato))
    
salarioMes()

