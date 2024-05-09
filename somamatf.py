#// -*- coding: utf-8 -*-//
# Programa: somamatf.py
# Programador: Beatriz
# Data:09/05/2024
# Este Programa lê duas matrizes de inteiros, calcula a soma das
def main():
    # Lendo as dimensões da matriz
    m, n = map(int, input().split())

    # Inicializando as matrizes a e b
    a = []
    b = []

    # Lendo os elementos da matriz a
    for _ in range(m):
        linha = list(map(int, input().split()))
        a.append(linha)

    # Lendo os elementos da matriz b
    for _ in range(m):
        linha = list(map(int, input().split()))
        b.append(linha)

    # Inicializando a matriz c com zeros
    c = [[0] * n for _ in range(m)]

    # Calculando a soma das matrizes
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]

    # Imprimindo a matriz soma
    print(c)

if __name__ == "__main__":
    main()
