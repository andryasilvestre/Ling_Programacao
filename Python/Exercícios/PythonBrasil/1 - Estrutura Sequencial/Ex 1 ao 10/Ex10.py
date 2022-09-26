# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def conversorTemp():
    tempCelsius = input("Informe a temperatura em Celsius: ")
    tempFahrenheit = round(32 + ((9 * float(tempCelsius)) / 5), 2)
    
    print(tempFahrenheit, "F")
    
conversorTemp()