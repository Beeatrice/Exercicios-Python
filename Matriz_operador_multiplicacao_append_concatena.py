# coding: utf-8
'''
Programa: Matriz_operador_multiplicacao_append_concatena.py
Programadora: Beatriz Sanabria
Data: 29/05/2023

    Cria e uma matriz com m linhas e n colunas
    com cada elemento inicializado com um valor lido.
    Uma matriz é uma lista de listas.
    Cada linha é uma lista de n colunas, e há m linhas.
'''

linhas = int(input('Digite a quantidade de linhas: ')) # Lê o número de linhas da matriz
colunas = int(input('Digite a quantidade de colunas: ')) # Lê o número de colunas da matriz
valor_inicial = int(input()) # Lê o valor de inicialização
matriz = [] # lista vazia
for i in range(calunas):
    # cria a linha i
    linha = [valor_inicial]*linhas # lista de n posições com valor armazenado em init
    # coloque linha na matriz
    matriz += [linha]
print(matriz)
