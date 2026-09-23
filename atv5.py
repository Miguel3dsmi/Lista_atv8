'''5. (ExeVetor05) Escreva um programa que possua dois vetores pré-preenchidos (A e B),
ambos de 10 posições. O programa deve fazer a multiplicação dos elementos de mesmo
índice em ambos os vetores e colocar o resultado no mesmo índice em um terceiro vetor
(C). Mostre o vetor C resultante.'''
import random
vetorA = [0] * 10
vetorB = [0] * 10
vetorC = [0] * 10
for i in range(len(vetorA)):
    vetorA[i] = random.randint(1, 100)
    vetorB[i] = random.randint(1, 100)
print(f"VetorA: {vetorA}\nVetorB: {vetorB}")
for i in range(len(vetorC)):
    vetorC[i] = vetorA[i] * vetorB[i]
print(f"\nVetorC: {vetorC}")
