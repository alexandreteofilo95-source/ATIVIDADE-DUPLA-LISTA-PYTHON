import os
os.system('cls')
numero_vetores = []
numero_vetor = []
soma = 0
NUMEROS_TENTATIVAS = 5
for calculo in range(NUMEROS_TENTATIVAS):
    numero = int(input(f'digite {calculo+1} inteiro A:'))
    numero_vetores.append(numero)

print('\n')
for i in range(NUMEROS_TENTATIVAS):
    numeros = int(input(f'digite {i+1} inteiro B:'))
    numero_vetor.append(numeros)
    
    


for numero_vetores, numero_vetor in enumerate(numero_vetor,start=1):
    print(f'A = {numero_vetores} + B = {numero_vetor}: C = {numero_vetores + numero_vetor}')