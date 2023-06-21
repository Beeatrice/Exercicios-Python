# -*- coding: utf-8 -*-

'''
Programa: Percurso_na_matriz.py 
Programadora: Beatriz Sanabria
Data: 21/06/2023

Deseja-se fazer percursos em uma matriz M mxn, de strings de tamanho 1, com m e n maiores ou iguais a 2, dirigidos por saltos definidos em um vetor de strings S, a partir de uma posição inicial (li, ci) em M.
Cada posição de S possui uma string de tamanho 3: a posição 0 indica se o salto é na linha (L) ou na coluna (C), a posição 1 indica se é incremento (+) ou decremento (-), e a posição 2 indica um deslocamento de 1 a 9 posições.
Deve-se percorrer S sempre a partir da posição zero para posições crescentes, à medida que os saltos são realizados em M. Deve-se parar o percurso se um novo salto levar a uma posição inválida de M. Considerar como posições válidas apenas as posições de [0, m-1] para linhas e [0, n-1] para colunas de M.

Entrada
Ler: uma linha com o número de linhas (m) e de colunas (n) de M, separados por espaços; m linhas com n valores string, de tamanho 1; uma linha com um vetor de strings S, separadas por espaços; e uma linha com uma posição inicial em M, li e ci, separados por espaços, com 0 <= li < m e 0 <= ci < n.
Saída
Uma linha de saída, com triplas (linha i em M, coluna j em M, M[i][j]) para o percurso em M a partir de (li, ci). As triplas não podem ter espaços entre elas, nem antes nem depois.


4 12
Universidade
Federal de M
ato Grosso d
o Sul - 2023
L+1 C+1 C+4 C+1 L+3
0 3
(0, 3, v)(1, 3, e)(1, 4, r)(1, 8, d)(1, 9, e)

4 12
Universidade
Federal de M
ato Grosso d
o Sul - 2023
C-2 C-3 C-1 C-3 L+1
1 11
(1, 11, M)(1, 9, e)(1, 6, l)(1, 5, a)(1, 2, d)(2, 2, o)

'''

def percurso_matriz(M, S, li, ci):
    # Função que realiza o percurso na matriz
    # Recebe a matriz M, o vetor de strings S, e as coordenadas iniciais li e ci
    
    m = len(M)  # Número de linhas da matriz M
    n = len(M[0])  # Número de colunas da matriz M
    percurso = []  # Lista para armazenar o percurso realizado
    
    for salto in S:  # Itera sobre cada salto definido no vetor S
        direcao = salto[0]  # Direção do salto (L para linha, C para coluna)
        incremento = salto[1]  # Incremento (+ para aumento, - para diminuição)
        deslocamento = int(salto[2])  # Número de posições a serem deslocadas
        
        if direcao == 'L':  # Se o salto for na linha
            if incremento == '+':  # Se for incremento
                li += deslocamento  # Atualiza a linha atual com o incremento
            else:  # Se for decremento
                li -= deslocamento  # Atualiza a linha atual com o decremento
        elif direcao == 'C':  # Se o salto for na coluna
            if incremento == '+':  # Se for incremento
                ci += deslocamento  # Atualiza a coluna atual com o incremento
            else:  # Se for decremento
                ci -= deslocamento  # Atualiza a coluna atual com o decremento
        
        if li < 0 or li >= m or ci < 0 or ci >= n:  # Verifica se as coordenadas estão dentro dos limites da matriz
            break  # Se não estiverem, encerra o percurso
        
        percurso.append((li, ci, M[li][ci]))  # Adiciona a tripla (linha, coluna, valor) no percurso
    
    return percurso  # Retorna o percurso realizado

# Leitura dos valores de entrada
m, n = map(int, input().split())  # Lê o número de linhas (m) e colunas (n) da matriz
M = []  # Lista para armazenar a matriz
for _ in range(m):  # Loop para ler cada linha da matriz
    linha = input()  # Lê a linha da matriz
    M.append(linha)  # Adiciona a linha na matriz

S = input().split()  # Lê o vetor de saltos S
li, ci = map(int, input().split())  # Lê as coordenadas iniciais li e ci

# Chamada da função para obter o percurso na matriz
resultado = percurso_matriz(M, S, li, ci)

# Impressão do resultado
for item in resultado:  # Itera sobre cada item do resultado
    print(f'({item[0]}, {item[1]}, {item[2]})', end='')  # Imprime a tripla (linha, coluna, valor)
