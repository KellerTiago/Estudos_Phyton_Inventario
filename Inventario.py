from selecionar_opcao import listar_opcoes
inventario = {}

opcao = listar_opcoes()

while opcao > 0 and opcao < 4:
    if opcao == 1:
        resp = "S"
        while resp == "S":
            inventario [input("Digite o numero patrimonial: ")] = [input("Digite a ultima data de atualização: "), input("Digite a descrição do bem: "), input("Digite o departamento: ")]
            resp = input("Digite S para continuar: ").upper()
    elif opcao == 2:
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write(f"{chave};{valor[0]};{valor[1]};{valor[2]};\n")
            print("Documento salvo com sucesso !")
    elif opcao == 3:
        with open("inventario.csv", "r") as inv:
            print(inv.readlines())
    opcao = listar_opcoes()
