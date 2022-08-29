# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius. 
# C = 5 * ((F-32) / 9).

def conversorTemp():
    tempFahrenheit = input("Informe a temperatura em Fahrenheit: ")
    tempCelsius = round((5 * ((float(tempFahrenheit) - 32) / 9)), 2)
    
    print(tempCelsius, "ºC")
    
conversorTemp()