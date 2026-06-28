# DESAFIO 016
# Crie a classe Funcionario, onde podemos cadastrar:
# nome, setor e cargo.
#
# Crie também um método que permita ao funcionário se apresentar.
class Funcionario():
    def __init__(self, nome, setor, cargo):
        
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentacao(self):
        print( f"Olá! Sou {self.nome}, atuo no setor {self.setor}, e sou {self.cargo}.")

f1 = Funcionario("Hugo Pierry","TI","Desenvolverdor Python")
f1.apresentacao()