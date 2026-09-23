'''7. (ExeVetor07) Ler um vetor X de 10 elementos (solicite ao usuário que digite os 10 valores
do tipo inteiro e armazene-os nas respectivas posições). Crie um vetor Y de tamanho 10
da seguinte forma: (a) Os elementos de ordem par de Y (índices 0, 2, 4, 6, 8) receberão os
respectivos elementos de X multiplicados por 2. (b) Os elementos de ordem ímpar de Y
(índices 1, 3, 5, 7, 9) receberão os respectivos elementos de X multiplicados por 3. Escrever
o vetor Y ao final.'''
X = [0] * 10
Y = [0] * 10

for i in range(len(X)):
    X[i] = int(input("Digite um valor: "))
for i in range(len(Y)):
    if i % 2 != 0:
        Y[i] = X[i] * 3
    else:
        Y[i] = X[i] * 2
print(Y)