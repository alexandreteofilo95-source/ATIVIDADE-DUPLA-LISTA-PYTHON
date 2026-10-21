import os

vetor_numeros = []
QUANTIDADE_DE_NUMEROS = 10
maiores = 0

for i in range(QUANTIDADE_DE_NUMEROS):
    numero = int(input(f"digite {i+1} numero "))
    vetor_numeros.append(numero)

soma = sum(vetor_numeros)



for numero in vetor_numeros:
    if numero > 10:
        maiores += 1




print(f"soma {soma}")
print(f"maiores {maiores}")
