# -*- coding: utf-8 -*-

'''
Programa: Soma_da_Ampulheta.py 
Programadora: Beatriz Sanabria
Data: 21/06/2023

Considere uma matriz quadrada de inteiros Q de ordem D, com D maior ou igual a 3; e a ampulheta formada pelas áreas superior e inferior das diagonais principal e secundária de Q. Os valores nas posições dessas diagonais também fazem parte da área da ampulheta. A partir dos dados de entrada, mostre a soma dos valores que formam a ampulheta.
Dica: até a linha (D-1) // 2, percorre-se da coluna da diagonal principal até a secundária para a ampulheta.

Entrada
Há vários casos de teste terminados por fim de arquivo (EOF). Em cada caso de teste há: a leitura de um inteiro D, com D maior ou igual a 3, em uma linha; e nas D linhas seguintes, a leitura dos D valores inteiros de cada linha da matriz Q separados por espaços.
Saída
Cada caso de teste deve mostrar a soma dos valores inteiros que formam a ampulheta.

3
1 2 3
2 4 6
10 20 30
4
2 2 2 2
3 3 3 3
4 4 4 4
5 5 5 5
70
42 
'''
while True:
  try:
    d = int(input())  # Vamos fazer a leitura do tamanho da matriz
    q = []  # Criei uma matriz Q como uma lista vazia.
    for i in range(d): # Aqui no loop é feita a leitura dos valores de cada linha da matriz e adicionado à lista Q.
      linha = list(map(int, input().split()))  # Leitura dos valores da linha i
      q.append(linha)  # adiciona a linha à matriz
    soma = 0  # variável para armazenar a soma dos valores da ampulheta
    for i in range(d): # É criada a variável soma, que irá armazenar a soma dos valores da ampulheta.
      for j in range(d): # Aqui é feito dois loop for para percorrer toda a matriz. Na condição do primeiro if, verifica se estou na área superior da ampulheta. Na condição do segundo if, verifico se estou dentro da ampulheta. Se sim, adicionamos o valor da posição à variável soma.
        if i <= (d-1)//2:  # verifica se está na área superior da ampulheta
          if j >= i and j <= d-1-i:  # verifica se está dentro da ampulheta
            soma += q[i][j]  # adiciona o valor à soma
        else:  # está na área inferior da ampulheta
          if j >= d-1-i and j <= i:  # verifica se está dentro da ampulheta
            soma += q[i][j]  # adiciona o valor à soma
    print(soma)  # exibe a soma dos valores da ampulheta
  except EOFError:  # Por fim aqui encerra o programa caso não haja mais entradas a serem lidas.

    break
