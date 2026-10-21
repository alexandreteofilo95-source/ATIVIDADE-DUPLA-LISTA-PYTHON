import os
os.system('cls')

numeros_vetores = []
NUMEROS_TENTATIVAS = 10
print('\n = INSERINDO DADOS =')
for i in range(NUMEROS_TENTATIVAS):
    numeros = int(input(f'digite {i+1} numero: '))
    
    if numeros < 0:
        resultado = numeros
    else:
        resultados = numeros
        numeros_vetores.append(numeros)

print('\n = RESULTADO DOS DADOS =')
for indice, resultados in enumerate(numeros_vetores,start=1):
    print(f'numeros positivos: {resultados} ')
print(f'\nnumeros copiados: {indice}')