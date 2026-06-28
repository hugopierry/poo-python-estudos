from rich import print
from rich.panel import Panel

print("olá [red]Mundo [/red]! :earth_americas:")
print("Olá, [bold blue on white]Pequeno Gafanhoto[/] :vulcan_salute:")
print(":+1: :-1:")
print("[red]Acesso negado![red]")

caixa = Panel(renderable="[white]Esse aqui é um painel de exemplo",title="Mensagem", style ="")

print(caixa)