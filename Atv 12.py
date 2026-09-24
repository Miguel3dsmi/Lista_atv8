'''12. (ExeVetor13) Faça um programa que declare e preencha (via teclado ou código) dois
vetores (A e B) de 30 posições cada. Crie um terceiro vetor (C) também de 30 posições
com a intersecção dos dois primeiros, isto é, coloque em C apenas os elementos que
existem tanto no vetor A quanto no vetor B (sem repetições). Mostre o vetor C.'''
import random
lista_A, lista_B, lista_C = [], [], []
tamanho = 30

for i in range(tamanho): #Adiciona elementos as listas
    lista_A.append(random.randint(1, 30))
    lista_B.append(random.randint(10, 40))

for i in range (len(lista_A)):
    for j in range (len(lista_B)):
        if lista_A[i] == lista_B[j]:
            if lista_A[i] not in lista_C:
                lista_C.append(lista_A[i])
            else:
                continue
        else:
            continue

print(f"Lista A: {lista_A}\nLista B: {lista_B}")
print(f"Lista de intersecção: {lista_C}")
