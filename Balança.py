def cadastrarProduto(codigo, tipo, descricao, preco):
    alinhamentoPreco = f"{preco:07.2f}".replace('.', '')
    return f"{codigo:06d}{tipo}{descricao:<22}{alinhamentoPreco}000"

produtosCadastrados = []

while True:
    codigo = int(input("Digite o código do produto (Digite até 6 digitos): "))
    tipo = input("Digite o tipo do produto (P ou U): ").upper()
    if tipo not in ["P", "U"]:
        print("Esse tipo de produto não existe, Insira apenas P para produtos de peso ou U para produtos de unidade.")
        print("O programa sera reiniciado para que você possa inserir o tipo correto.")
        continue
    descricao = input("Digite a descrição do produto (so sera cadastrado os 22 primeiros caracteres): ")[:22]
    preco = float(input("Digite o preço do seu produto: "))
    
    produtosCadastrados.append({"codigo": codigo, "tipo": tipo, "descricao": descricao, "preco": preco})
    
    continuarCadastro = input("Você deseja cadastrar outro produto? (Sim ou Nao): ")
    if continuarCadastro != "Sim":
        break

with open("CADTXT.TXT", "a") as arquivo:
    for produto in produtosCadastrados:
        linhaDeCadastro = cadastrarProduto(
            produto["codigo"],
            produto["tipo"],
            produto["descricao"],
            produto["preco"]
        )

        arquivo.write(linhaDeCadastro + "\n")

print("Seu arquivo CADTXT.TXT, Foi criado com sucesso!")
print("Verifique a pagina onde se encontra o programa.")