# coding: utf-8
'''
Programa: Matriz_operador_multiplicacao_append_int.py
Programadora: Beatriz Sanabria
Data: 26/05/2023

Cria e uma matriz com m linhas e n colunas
com cada elemento inicializado com um valor lido.
Uma matriz é uma lista de listas.
Cada linha é uma lista de n colunas, e há m linhas.

'''
linhas = int(input('Digite o número de linhas de sua matriz: ')) # Lê o número de linhas da matriz
colunas = int(input('Digite o número de colunas de sua matriz: ')) # Lê o número de coluna da matriz
valor_inicial = int(input('Digite o número para inicializar: ')) # Lê o valor de inicialização
matriz = [] # lista vazia

for i in range(linhas): # cria a linha i
  linha = [valor_inicial]*colunas # lista de n posições com valor armazenado em valor_inicial
  matriz.append(linha) # coloque linha na matriz
print('Sua matriz com números inteiros ficou assim:',matriz)
