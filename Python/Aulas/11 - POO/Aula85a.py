# Herança --- > reaproveitamento de código // classes distintas que contém os mesmos atributos

class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        
    def nomeCompleto(self):
        print(self.nome, self.sobrenome)
        
p1 = Pessoa('Maggie', 'May')
p1.nomeCompleto()

# class Estudante(Pessoa):
#         pass

# class Estudante(Pessoa):
#     def __init__(self, nome, sobrenome):
#         Pessoa.__init__(self, nome, sobrenome)    # referencia direta à classe

class Estudante(Pessoa):
    def __init__(self, nome, sobrenome):
        super().__init__(nome, sobrenome)     # herda todos os comportamentos super() 
        
  
p2 = Estudante('Petunia', 'May')
p2.nomeCompleto()

    # Adicionar propriedades e métodos