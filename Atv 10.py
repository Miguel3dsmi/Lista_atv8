'''10. (ExeVetor10) Escreva um programa que leia diversos números inteiros fornecidos pelo
usuário e distribua esses valores entre dois vetores: o vetor_impares e o vetor_pares. Cada
um terá o tamanho fixo de 10 posições. A repetição do algoritmo se dará até que o usuário
digite o número zero (0) ou até que um dos vetores tenha sido totalmente preenchido.
Mostre o conteúdo válido dos dois vetores no final.'''
vetor_impares, vetor_pares  = [], []
tamanho = 10
numero = 1
while numero != 0 and (len(vetor_pares) < tamanho and len(vetor_impares) < tamanho):
    for i in range (20):
        numero = int(input("Digite um Nº: "))
        if numero == 0:
            break
        else:
            if i < 10:
                if numero % 2 == 0:
                    vetor_pares.append(numero)
                else:
                    vetor_impares.append(numero)
            else:
                if numero % 2 == 0:
                    vetor_pares.append(numero)
                else:
                    vetor_impares.append(numero)
print(f"Lista de vetores Pares: {vetor_pares}\nLista de vetores Impares: {vetor_impares}")