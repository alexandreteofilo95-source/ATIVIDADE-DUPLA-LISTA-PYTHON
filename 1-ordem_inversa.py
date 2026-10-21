import os
print("feito por andre")
print("ra 026.074752")

vetor_numero = []
QUANTIDADE_DE_NUMERO = 5

for i in range(QUANTIDADE_DE_NUMERO):
    numero = int(input(f"digite {i+1} numero "))
    vetor_numero.append(numero)

for numeros, numero in enumerate(vetor_numero, start= 1 ):
    print(f"numeros digitados {numero}")


for  numero in range (5,0,-1):
    print(f"ordem inversa {numero}")
