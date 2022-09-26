a = 'Ândrya'
b = "Maggie, Freddie e Petunia"
c = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Aliquam cursus aliquam neque efficitur sollicitudin. 
Duis eu pharetra neque. 
Sed quis ultricies lorem..."""
d = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Aliquam cursus aliquam neque efficitur sollicitudin. 
Duis eu pharetra neque. 
Sed quis ultricies lorem... '''

# print(d)

e = "Olá, mundo!"

#indexação = acessar o elemento X do dado
print(e[1])
print("\n")

# for x in "Ândrya": 
#     print(x)
    
# x = len(e)
# print(x)

txt =  "Seja bem-vinda ao curso de Python!"
x = "vinda" in txt

print(x) 
print("carro" in txt)

if "teste" in txt:
    print("Sim. 'vinda' está presente...")
if "teste" not in txt:
    print("Não. 'teste' não está presente...")
    
# else:                                           
#   print("a palavra não está presente.")       
