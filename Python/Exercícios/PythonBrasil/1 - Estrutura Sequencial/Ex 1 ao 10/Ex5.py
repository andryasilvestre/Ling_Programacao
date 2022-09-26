# Faça um Programa que converta metros para centímetros.

def conversor():
    metro = input("Informe a metragem: ")
    cm = float(metro)/100.
    
    print(float(metro), "metros tem", round(cm, 4), "centímetros.")

conversor()