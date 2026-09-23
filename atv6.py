'''6. (ExeVetor06) Escreva um programa que declare e inicialize diretamente no código um
vetor de 10 posições contendo números inteiros (positivos e negativos). O programa deve
mostrar somente os números positivos acompanhados de suas respectivas posições
(índices).'''
import random
lista_completa = [0] * 10
lista_positivos = []
posicao = []
for i in range(len(lista_completa)):
    lista_completa[i] = random.randint(-10, 10)
    if lista_completa[i] > 0:
        lista_positivos.append(lista_completa[i])
        posicao.append(i)

print("A lista de números positivos e seus respectivas posições: ")
for i in range(len(lista_positivos)):
    print(f"Nº: {lista_positivos[i]} index: {posicao[i]}")