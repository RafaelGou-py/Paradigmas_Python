def concatenacao(PrimPalavra, SegPalavra):
    
    for NovaPalavra in SegPalavra:
        PrimPalavra += NovaPalavra

    return PrimPalavra

PrimPalavra = "Ola "
SegPalavra = "Viajante, "
TerPalavra = "Bem-Vindo!"

execucao1 = concatenacao(PrimPalavra, SegPalavra)
execucaoFinal = concatenacao(execucao1, TerPalavra)

print(execucaoFinal)