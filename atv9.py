'''9. (ExeVetor09) Escreva um programa que crie, em tempo de compilação, 2 vetores (A e B)
de 10 elementos inteiros cada. Após isso, o programa deverá criar um terceiro vetor (C),
de 20 posições, que seja a união dos dois primeiros, ou seja, as primeiras 10 posições de
C recebem o vetor A, e as últimas 10 recebem o vetor B. Mostre o vetor resultante.'''
A, B, C = [0] * 10,[0] * 10,[0] * 20

for i in range(len(A)):
    A[i] = i+1
for i in range(len(B)):
    B[i] = i+11

for i in range(len(C)):
    if i < len(A):
        C[i] = A[i]
    else:
        C[i] = B[i -len(A)]
print(C)