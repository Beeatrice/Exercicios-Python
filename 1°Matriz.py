# coding: utf-8
'''
    Programa: 1°Matriz.py
    Programadora: Beatriz Sanabria
    Data: 24/05/2023
    
    Cria uma matriz com m linhas e n colunas
    com cada elemento inicializado com um valor lido.
    Uma matriz é uma lista de listas.
    Cada linha é uma lista de n colunas, e há m linhas.
'''

m = int(input("Número de linhas da matriz:")) #Lê o número das linhas da matriz
n = int(input("Número de colunas da matriz:")) # Lê o número das colunas da matriz 
mat = [] # Lista vazia
for i in range(m): # Cria a linha i
    linha = [0]*n # as posições são todas inicializadas com 0
# Depois coloque linha na matriz
    mat.append(linha)
print(mat)

# Lê cada posição da matriz
print("Leitura de cada posição da matriz:")
for i in range(m):
    for j in range(n):print("Matriz[%d][%d] = " % (i, j), end = "")
    mat[i][j] = int(input())

# Mostra cada posição da matriz
print("Mostra cada posição da matriz:")
for i in range(m):
    for i in range(n):
        print("Matriz [%d][%d] = %d" % (i, j, mat[i][j]))

print("Mostra a matriz em formato mais amigável:")
for i in range(m): 
    for i in range(n): 
        print(" "+ str(mat[i][j]), end="")
    print()
