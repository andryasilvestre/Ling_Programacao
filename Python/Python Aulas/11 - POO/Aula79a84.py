class MinhaClasse:
    x = 5
    
print(MinhaClasse)
p1 = MinhaClasse
print(p1.x)

class Pessoa:
    def __init__(self, nome, idade, raca, descricao) -> None:       # parametro de entrada
        self.nome = nome 
        self.idade = idade 
        self.raca = raca 
        self.descricao = descricao
        
    # o self pode ser qualquer outro nome, desde que seja o primeiro parametro
    def funcao(self):
        print('Olá, meu nome é', self.nome)
        
p1 = Pessoa('Maggie', 4, 'Shih-Tzu', 'Lombinho')
p1.funcao()
print(p1.nome)


# modificar propriedade de objetos e declaração de passagem

p1.nome = 'Charmene'
p1.funcao()
print("Nome:", p1.nome)

# del exclui completamente da memória

del p1.raca
del p1
print(p1)