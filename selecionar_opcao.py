def listar_opcoes ():
    opcao = int(input("Digite:\n (1) para registrar um ativo:\n (2) para salvar em arquivo:\n (3) para exibir os arquivos armazenados:"))
    return opcao

def registrar (inventario):
    resp = "S"
    while resp == "S":
        inventario [input("Digite o numero patrimonial: ")] = [input("Digite a ultima data de atualização: "), input("Digite a descrição do bem: "), input("Digite o departamento: ")]
        resp = input("Digite S para continuar: ").upper()
def persistir (inventario):
    with open("inventario.txt", "a") as inv:
        for chave, valor in inventario.items():
            inv.write(f"{chave};{valor[0]};{valor[1]};{valor[2]}\n")
    return "Salvo com sucesso"
def exibir ():
    with open("inventario.csv", "r") as inv:
        linhas = inv.readlines()
    for linha in linhas:
        separacao=linha[linha.find(";")+1:-1]
        data=separacao[0:separacao.find(";")]
        separacao = separacao[separacao.find(";")+1:-1]
        descricao=separacao[0:separacao.find(";")]
        departamento=linha[linha.rfind(";")+1:-1]
        print ("Data.........: ", data)
        print("Descrição....: ", descricao)
        print("Departamento.: ", departamento)




