# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a 
# quantidades de latas de tinta a serem compradas e o preço total.

areaPintar = float(input("Qual a área(m²) a ser pintada? "))

galoesUsados = 0
if ((areaPintar // 54) == 0 and (areaPintar != 0)):
    galoesUsados = 1
elif ((areaPintar // 54) >= 1 and (areaPintar % 54) == 0):
    galoesUsados = (areaPintar // 54) 
elif ((areaPintar // 54)>= 1 and (areaPintar % 54) != 0): 
    galoesUsados = (areaPintar // 54) + 1

precoTotal = (galoesUsados * 80)
    
print("\n" + "A quantidade de latas a serem compradas é igual à", galoesUsados)
print("O preço total é de R$", precoTotal)
