'''8. (ExeVetor08) Ler um vetor M de 10 elementos (solicite ao usuário que digite os 10 valores
inteiros) e imprima a lista original. A seguir, troque fisicamente na memória o valor do 1o
elemento (índice 0) com o 6o (índice 5), o 2o com o 7o, e assim por diante até o 5o com
10o. Escreva o vetor M após a modificação.'''
M =[0] * 10
for i in range(len(M)):
    M[i] = int(input("Digite um valor: "))
print(M)
for t in range(5):
    M[t], M[t+5] = M[t+5], M[t]
print(M)