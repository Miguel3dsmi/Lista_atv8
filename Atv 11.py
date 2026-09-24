'''11. (ExeVetor12) Elabore um programa que leia pelo teclado um vetor de 6 posições de
números inteiros. Após a leitura, exiba o menu a seguir e peça para o usuário digitar uma
variável identificadora (1, 2, 3 ou 4). O programa deve calcular a operação correspondente
à opção escolhida:
Escolha a opção desejada:
1. Soma dos elementos
2. 2- Produto (multiplicação) dos elementos
3. 3- Média dos elementos
4. 4- Mostrar o vetor
5. ?'''
lista = []
tamanho = 6
for i in range(tamanho):
    numero = int(input("Digite um Nº: "))
    lista.append(numero)
print(f"\nEscolha uma das opções abaixo:\n1. Soma dos elementos\n2. Produto dos elementos\n3. Média dos elementos\n4. Mostrar o vetor\n5. Sair")
while True:
    choice = int(input())
    match choice:
        case 1:
            soma = sum(lista)
            print(soma)
            break
        case 2:
            produto = 1
            for e in range(len(lista)):
                produto = produto * lista[e]
            print(produto)
            break
        case 3:
            soma = sum(lista)
            media = (soma / tamanho)
            print(media)
            break
        case 4:
            print(lista)
            break
        case 5:
            print("Saindo...")
            break
        case _:
            print("Opção invalida!")