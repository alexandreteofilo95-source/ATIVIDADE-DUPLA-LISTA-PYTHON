import os
os.system('cls')

print('feito por: Alexandre Teofilo França')
print('R.A.:026.072334')
NUMEROS_TENTATIVAS = 7
numero_vetor = []

numero_vetor.append(22)
numero_vetor.append(23)
numero_vetor.append(24)
numero_vetor.append(26)
numero_vetor.append(28)
numero_vetor.append(25)
numero_vetor.append(30)
maior = max(numero_vetor)
menor = min(numero_vetor)

for indice, i in enumerate(numero_vetor, start=1):
    print(f' {indice} dia fez: {i} graus')
    media = 28/7
print(f'\nmedia dos dias na semana: {media}')
print(f'maior temperatura: {maior}')
print(f'menor temperatura: {menor}')