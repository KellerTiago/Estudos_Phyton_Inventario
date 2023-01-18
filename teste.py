linhas =['12;31/12/2022;CONTROLE;keller']

resultado = map(lambda x: x.upper(), linhas)
print(list(resultado))

for linha in linhas:
    separacao=linha[linha.find(";")+1:-1]
    print(separacao)
    print(type(separacao))
    data=separacao[0:separacao.find(";")]
    print(data)
    separacao = separacao[separacao.find(";")+1:-1]
    print(separacao)
    descricao=separacao[0:separacao.find(";")]
    print(descricao)
    departamento=linha[linha.rfind(";")+1:-1]
    print(departamento)
    print ("Data.........: ", data)
    print("Descrição....: ", descricao)
    print("Departamento.: ", departamento)
    print(type(linhas))
