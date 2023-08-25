def subpalavra(Palavra, inicio, fim):
    NovaPalavra = ""

    for i in range(inicio, fim):
        NovaPalavra += Palavra[i]

    return NovaPalavra

Palavra = "Rafael"
inicio = 0
fim = 4

execucao = subpalavra(Palavra, inicio, fim)
print(execucao)