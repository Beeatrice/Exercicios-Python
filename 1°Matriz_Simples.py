# coding: utf-8
'''
    Programa: 1°Matriz.py
    Programadora: Beatriz Sanabria
    Data: 24/05/2023
    
    Cria e uma matriz com a variavel linhas para as linhas e colunas para as colunas
    com cada elemento inicializado com um valor lido.
    Uma matriz é uma lista de listas.
    Cada linha é uma lista de n colunas, e há m linhas.
'''
linhas = int(input('Digite a quantidade de linhas da matriz:')) # Lê o número de linhas da matriz
colunas = int(input('Digite a quantidade de colunas da matriz:')) # Lê o número de colunas da matriz
inicial = int(input()) # Lê o valor de inicialização
matriz = [] # lista vazia
for i in range(linhas): # cria a linha i
    linha = [] # lista vazia
    for j in range(colunas): # Cria uma linha que é uma lista com m colunas
        linha.append(inicial) # Cada posição tem o valor lido em inicial como elemento 
        # coloque linha na matriz
    matriz.append(linha)
    print(matriz)
