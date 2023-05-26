# coding: utf-8
# Programa: Matriz_operador_multiplicacao_append_bool.py
# Programadora: Beatriz Sanabria
# Data: 26/05/2023

'''
    Cria e uma matriz com m linhas e n colunas
    com cada elemento inicializado com um valor lido.
    Uma matriz é uma lista de listas.
    Cada linha é uma lista de n colunas, e há m linhas.
'''

def to_bool(val):
  if val == "False":
    return False 
  else: # Assumindo que a entrada será "True" ou "False"
    return True 

linhas = int(input()) # Lê o número de linhas da matriz
colunas = int(input()) # Lê o número de colunas da matriz
valor_inicial = to_bool(input()) # Lê o valor de inicialização
matriz = []

for i in range(linhas): # cria a linha i
  linha = [valor_inicial]*colunas # lista de n posições com valor armazenado em init
  matriz.append(linha) # coloque linha na matriz
print(matriz)
