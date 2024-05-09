# -*- coding: utf-8 -*-
# Programa: cubo.py
# Programador: Beatriz 
# Data: 09/05/2024
# Este programa lê um valor real, calcula o o cubo e imprime o resultado.
# O programa usa a função cubof para calcular o cubo de x

def main():
    # Lendo o número float de entrada
    x = float(input())

    # Calculando o cubo do número
    resultado = round(x ** 3, 2)

    # Imprimindo o resultado com duas casas decimais
    print("{:.2f}".format(resultado))

if __name__ == "__main__":
    main()
