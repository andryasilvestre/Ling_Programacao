"""
Variáveis criadas DENTRO do bloco da função é LOCAL
                  FORA do bloco é GLOBAL
"""
# para criar funcao é ' def '
# primeiro ele procura pela variável local. Caso não tenha, utiliza a global

x = "incrível"

def myFunc():
    x = "fantástico"
    print("Python é " + x)
    
    global z 
    z = "Bem-vinda ao curso!"

# chamar a função.    
myFunc()

print("\n" + z)
print("Você é " + x)
