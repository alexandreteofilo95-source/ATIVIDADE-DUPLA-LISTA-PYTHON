import os
os.system('cls')
NUMEROS_TENTATIVAS = 3
numeros_vetores = []
numeros_vetor = []

for i in range(NUMEROS_TENTATIVAS):
    nome = input('digite seu nome: ')
    salario = int(input('Digite seu salario: '))
    
    numeros_vetores.append(nome)
    numeros_vetor.append(salario)

    maior = max(numeros_vetor)
    menor = min(numeros_vetor)
    os.system('cls')

for indice, numeros_vetor in enumerate(numeros_vetores,start=1):
    print(f'nome: {numeros_vetor}, salario: {salario}')
print(f'{numeros_vetor} maior salario {maior}')
print(f'{numeros_vetor} maior salario {menor}')