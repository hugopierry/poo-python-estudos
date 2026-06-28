# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de intância
        self.nome =""
        self.idade = 0

    # Métodos de intância   
    def aniversario(self):
        self.idade = self.idade  + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhato(a) e tem {self.idade} anos de idade." 

# Declaração de objetos
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53

print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())

g4 = Gafanhoto()
g4.nome = "Hugo Pierry"
g4.idade = 34
g4.aniversario()
print(g4.mensagem())