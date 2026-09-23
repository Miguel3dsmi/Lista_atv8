'''4. (ExeVetor04) Escreva um programa que declare e inicialize diretamente no código
(estaticamente) um vetor de 20 posições contendo números inteiros. A seguir, usando um
laço de repetição, conte e diga quantos valores pares existem dentro deste vetor.'''
import random
vetorA = [0] * 20
contador = 0
for i in range(len(vetorA)):
    vetorA[i] = random.randint(1, 100)
print(f"A lista: {vetorA}")
for i in range(len(vetorA)):
    if vetorA[i] % 2 == 0:
        contador += 1
print(f"Possui {contador} valores pares.")