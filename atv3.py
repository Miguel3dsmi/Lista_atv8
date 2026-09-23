'''3. (ExeVetor03) Preencher um vetor B de 10 posições usando um laço de repetição com o
número 10 se o índice do elemento for ímpar, e com o número 20 se o índice for par.
Escrever o vetor B após o seu total preenchimento.'''
vetorB = [0] * 10
valor = 0
for i in range(len(vetorB)):
    vetorB[i] = valor
    if vetorB[i] % 2 != 0:
        vetorB[i] = 10
    else:
        vetorB[i] = 20
    valor += 1
print(vetorB)