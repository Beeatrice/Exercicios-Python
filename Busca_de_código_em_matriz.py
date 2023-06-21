# -*- coding: utf-8 -*-

'''
Programa: Busca_de_código_em_matriz.py 
Programadora: Beatriz Sanabria
Data: 21/06/2023

Considere uma matriz quadrada Q, de ordem D, composta por 0s e 1s que representam um código definido pelo usuário do programa; e uma matriz M de L linhas e C colunas, composta por strings de tamanho 1. Faça um programa que procure o código Q em M, e indique qual é a linha e coluna, em M, do canto superior esquerdo da primeira ocorrência do código em M. Um código Q estará em M se e somente se todos os seus valores aparecem exatamente na mesma configuração em M, considerando os 0s e 1s.
Entrada
A ordem D em uma linha, seguida de D linhas do código Q, com os valores 0 e 1 separados por espaços. D é maior ou igual a 2. A quantidade L de linhas e a quantidade de C de colunas de M, informadas em uma mesma linha e separadas por espaço, com L e C sendo números inteiros maiores ou iguais a 2. A seguir, é dada a matriz M, com L linhas e os valores separados por espaços.
Saída
A saída pode ser "Código encontrado em (x,y)", onde x e y são, respectivamente, a linha e a coluna em que o código foi encontrado em M, com 0 <= x < L e 0 <= y < C; ou a saída pode ser "Código não encontrado", quando o código Q não estiver em M.
Samples Input	Samples Output
2
1 1
1 0
5 7
* ( 1 0 1 1 1
0 1 1 % 7 0 0
1 1 x . 9 ) <
1 2 ; t A 4 8
F i n a l ! ?

Código não encontrado

2
1 1
1 0
5 7
* ( 1 0 1 1 1
0 1 1 % 7 0 0
1 1 0 . 9 ) <
1 0 ; t A 4 8
F i n a l ! ?

Código encontrado em (1,1)

'''
d = int(input()) # Lê a ordem do código
q = [] # CriEI uma lista vazia para a matriz Q
for i in range(d):
    line = input().split() # Li uma linha da matriz Q como uma string e divide em uma lista de elementos
    q.append(line) # Adiciono a linha na matriz Q

l, c = map(int, input().split()) # Entrada com quantidade de linhas e colunas da matriz M
m = [] # Criei mais uma lista vazia para a matriz M
for i in range(l):
    line = input().split() # Aqui lemos uma linha da matriz M como uma string e divide em uma lista de elementos
    m.append(line) # Adiciono com o append a linha na matriz M

found = False # Cria uma variável de controle para indicar se o código Q foi encontrado em M
for i in range(l-d+1):
    for j in range(c-d+1): # itera sobre todas as possíveis posições em M para encontrar Q
        match = True # Criei uma variável para indicar se o código Q foi encontrado na posição atual
        for y in range(d):
            for x in range(d): # itera sobre todos os elementos de Q na posição atual
                if m[i+y][j+x] != q[y][x]: # Na condição if se um elemento de M for diferente de um elemento de Q, não é uma correspondência
                    match = False
        if match: # E se todos os elementos de Q correspondem aos elementos de M na posição atual, encontramos Q
            found = True
            print("Código encontrado em ({},{})".format(i,j)) # exibe a posição encontrada
            break # Break interrompe a busca
    if found:
        break # interrompe a busca
if not found: # se Q não foi encontrado, exibe uma mensagem
    print("Código não encontrado")
