from selecionar_opcao import *
inventario = {}

opcao = listar_opcoes()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        registrar(inventario)
    elif opcao == 2:
        persistir(inventario)
    elif opcao == 3:
        exibir()
    opcao = listar_opcoes()
