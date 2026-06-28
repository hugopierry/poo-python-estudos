# DESAFIO 017
# Crie a classe Produto, onde podemos cadastrar:
# nome e o preço.
#
# Crie também um método que mostre uma etiqueta de preço do produto.

# f"{self.nome:^30}\n{"":-^30}\n{self.preco:.^30,.2f}",title="Produto",width=35)
from rich import print
from rich.panel import Panel
class Produto():
    def __init__(self,marca, descricao, preco):
        self.marca = marca
        self.descricao = descricao
        self.preco = preco
    
    def etiqueta(self):
        print( Panel( f"[blue]Marca:[/blue]{self.marca}\n[blue]Descrição:[/blue] {self.descricao}\n[blue]Preço:[/blue] R${self.preco:.2f}",title="Dados do produto",width=35))
        

p1 = Produto("Sansung","Galaxy S20 FE", 3500.00)

p1.etiqueta()

input("\n\n\n\n\nPressione ENTER para sair do programa")



