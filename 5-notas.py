import os

vetor = []
QUANTIDADE_DE_NUMEROS = 5

for i in range(QUANTIDADE_DE_NUMEROS):
    notas = float(input(f"digite a nota {i+1} "))
    vetor.append(notas)

media = sum(vetor) / 5

acima_da_media = 0
for notas in vetor:
    if notas > media:
        acima_da_media += 1


for exibição, notas in enumerate(vetor, start =1):
    print(f"\nnotas digitadas {notas}")

print(f"\nmedia da turma {media}")

for indice, media in enumerate(vetor):
        print(f"quantas notas ficaram acima da media = {acima_da_media} ")
