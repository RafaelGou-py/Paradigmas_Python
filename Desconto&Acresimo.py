class Item:

    def __init__(respec, codigo, descricao, valor, acrescimo=0, desconto=0):
        respec.codigo = codigo
        respec.descricao = descricao
        respec.valor = valor
        respec.acrescimo = acrescimo
        respec.desconto = desconto
        respec.total = valor + acrescimo - desconto

class Carrinho:

    def __init__(respec):
        respec.itens = []
        respec.acrescimo_total = 0
        respec.desconto_total = 0

    def insere_item(respec, codigo, descricao, valor):
        item = Item(codigo, descricao, valor)
        respec.itens.append(item)

    def acrescenta_item(respec, codigo, acrescimo):
        for item in respec.itens:
            if item.codigo == codigo:
                item.acrescimo += acrescimo
                item.total = item.valor + item.acrescimo - item.desconto
                break

    def descontar_item(respec, codigo, desconto):
        for item in respec.itens:
            if item.codigo == codigo:
                item.desconto += desconto
                item.total = item.valor + item.acrescimo - item.desconto
                break

    def acrescenta_total(respec, acrescimo_total):
        respec.acrescimo_total += acrescimo_total
        distribuir_acrescimo = acrescimo_total / len(respec.itens)
        for item in respec.itens:
            item.acrescimo += distribuir_acrescimo
            item.total = item.valor + item.acrescimo - item.desconto

    def descontar_total(respec, desconto_total):
        respec.desconto_total += desconto_total
        distribuir_desconto = desconto_total / len(respec.itens)
        for item in respec.itens:
            item.desconto += distribuir_desconto
            item.total = item.valor + item.acrescimo - item.desconto

    def finaliza_venda(respec):
        print("Itens adicionados no carrinho:")
        for item in respec.itens:
            print(f"Código: {item.codigo}, Descrição: {item.descricao}, Valor: R$ {item.valor:.2f}, Acréscimo: R$ {item.acrescimo:.2f}, Desconto: R$ {item.desconto:.2f}, Total: R$ {item.total:.2f}")

        print(f"Desconto total: R$ {respec.desconto_total:.2f}")
        print(f"Acréscimo total: R$ {respec.acrescimo_total:.2f}")

        valor_total = sum(item.total for item in respec.itens) + respec.acrescimo_total - respec.desconto_total
        print(f"Valor total: R$ {valor_total:.2f}")

carrinho = Carrinho()

while True:

    print("\nMenu Do Sistema de Vendas:")
    print("1 - Inserir item ao carrinho")
    print("2 - Acréscimo de item")
    print("3 - Desconto de item")
    print("4 - Acréscimo total")
    print("5 - Desconto total")
    print("6 - Finalizar venda")
    escolhaMenu = input("Escolha uma opção do Menu: ")

    if escolhaMenu == '1':
        codigo = input("Digite o código do produto: ")
        descricao = input("Digite a descrição do produto: ")
        valor = float(input("Digite o valor do produto: "))
        carrinho.insere_item(codigo, descricao, valor)

    elif escolhaMenu == '2':
        codigo = input("Digite o código do produto: ")
        acrescimo = float(input("Digite o valor do acréscimo do item: "))
        carrinho.acrescenta_item(codigo, acrescimo)

    elif escolhaMenu == '3':
        codigo = input("Digite o código do produto: ")
        desconto = float(input("Digite o valor do desconto do item: "))
        carrinho.descontar_item(codigo, desconto)

    elif escolhaMenu == '4':
        acrescimo_total = float(input("Digite o valor do acréscimo total: "))
        carrinho.acrescenta_total(acrescimo_total)

    elif escolhaMenu == '5':
        desconto_total = float(input("Digite o valor do desconto total: "))
        carrinho.descontar_total(desconto_total)

    elif escolhaMenu == '6':
        carrinho.finaliza_venda()
        break

    else:
        print("Opção inválida. Tente inserir um dos numeros do Menu.")
