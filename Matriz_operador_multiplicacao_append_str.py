# coding: utf-8
'''
Programa: Matriz_operador_multiplicacao_append_str.py
Programadora: Beatriz Sanabria
Data: 26/05/2023

    Cria e uma matriz com m linhas e n colunas
    com cada elemento inicializado com um valor lido.
    Uma matriz é uma lista de listas.
    Cada linha é uma lista de colunas, e linhas.
'''
linhas = int(input('Quantidade de linhas da matriz: ')) # Lê o número de linhas da matriz
colunas = int(input('Quantidade de colunas da matriz: ')) # Lê o número de coluna da matriz
valor_inicial = (input('Caractere ou str para inicializarmos: ')) # Lê o valor de inicialização
matriz = [] # lista vazia
for i in range(linhas)

  linha = [valor_inicial]*colunas
  matriz.append(linha)
  print('Sua matriz de str ficou asssim:',matriz)
