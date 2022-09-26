'''
upper, lower
replace, strip, split (transforma em lista)
'''

nome = "Ândrya Silvestre"
b = nome.upper()

print(nome[:7])
print(nome[7:])

# Começa a contar do final // fatiar strings
print(nome[-5:-2])

fatiaNome = nome[3:9]
print(fatiaNome)

print("\n\n")

# Modificar strings 
print(b)
print(nome.lower())

nome3 = "      Ândrya Silvestre     "
print(">" + nome3.strip() + "<")
print(nome3.strip())

nome4 = "Ândrya Silvestre"
print(nome4.replace("a", "4"))
print("\n\n")

a = "Carro, Moto, Caminhão"
print(a.split(","))

x1 = "Ândrya"
x2 = "Silvestre"
x3 = x1 + " " + x2

print(x3)