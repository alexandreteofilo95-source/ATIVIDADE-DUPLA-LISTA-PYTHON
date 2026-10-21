import os

vetor_numeros = []
QUANTIDADE_DE_NUMEROS = 8

for i in range(QUANTIDADE_DE_NUMEROS):
    numeros = int(input(f"digite o {i+1}° numero "))
    vetor_numeros.append(numeros)

pesquisa = input("pesquise um numero ")





for indice, numeros in enumerate(vetor_numeros):
    if numeros == pesquisa:
        achou = True, print("o numero existe")
    print(f"numero pesquisado {pesquisa}|")

if pesquisa in vetor_numeros:
    print("este numero existe")
posicao = vetor_numeros.index(pesquisa)
print(f"o numero existe {pesquisa} e esta na posição {posicao}")

