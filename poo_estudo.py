

#self sempre se refere ao objeto que está sendo criado. É o que diferencia os dados de p1 dos dados de p2.

# Métodos

# Métodos são funções que pertencem à classe. Eles sempre recebem self como primeiro parâmetro.

# Classe PAI — produto normal
class Produto:
    def __init__(self, nome,codigo, quantidade):
        
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
    
    def entrada(self, qtd):
        self.quantidade += qtd
    
    def saida(self, qtd):
        self.quantidade -= qtd
    
    def saldo(self):
        return f"{self.nome}: {self.quantidade} unidades"
    
    def __str__(self):
        return f"{self.codigo} - {self.nome} | {self.quantidade} unidades"
    
# classe FILHA - produto perecível  
class ProdutoPerecivel(Produto):
    def __init__(self, nome , codigo, quantidade, validade):
        super().__init__(nome, codigo, quantidade) # herda tudo
        self.validade = validade


p = ProdutoPerecivel("Whey","L001",20,"01-08-2028")
p.entrada(30)
p.saida(18)
print(p.saldo())
print(f"Validade: {p.validade}")
print(p)

#  Os 4 pilares que você já tocou hoje:Os 4 pilares que você já tocou hoje:

# Classe e objeto — Produto com __init__ e atributos ✅
# Métodos — entrada, saida, saldo ✅
# __str__ — exibição legível do objeto ✅
# Herança — ProdutoPerecivel herdando de Produto com super() ✅







    

    
