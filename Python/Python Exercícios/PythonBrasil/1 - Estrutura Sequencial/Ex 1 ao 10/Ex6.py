# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

def area():
    raio = input("Digite o raio do círculo: ")
    pi = math.pi
    area = pi * (float(raio)**2)
    
    print("A área do círculo é:", round(area, 2))
    
area()