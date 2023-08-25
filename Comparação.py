def comparacao(PrimPalavra, SegPalavra):
    if len(PrimPalavra) != len(SegPalavra):
        return False
    
    for i in range(len(PrimPalavra)):
        if PrimPalavra[i] != SegPalavra[i]:
            return False
        
    return True
    
while True:
    PrimPalavra = input("Digite a primeira palavra: ")
    SegPalavra = input("Digite a segunda palavra: ")

    execucao = comparacao(PrimPalavra, SegPalavra)

    if execucao:
        print("As palavras comparadas são exatamente iguais!")
    else:
        print("As palavras são diferente em tamanho ou letras!")
        print("Encerrando a execução do programa!")
        break
