 # -*- coding: utf-8 -*-
 # Programa: sucessores_inteiros.py
 # Programadora: Beatriz Sanabria
 # Data: 24/04/2023

valor_int = int(input())  # lê o valor inteiro
contador = 0  # contador para controlar a quantidade de números ímpares já impressos
while contador < 6:  # enquanto o contador for menor que 6 continua a verificação de verdadeiro ou falso (par ou impar)
    if valor_int % 2 == 1:  # se o valor_int dividido por 2 for igual a 1 quer dizer que o numero é impar pule para o print
        print(valor_int) # print o valor 
        contador += 1 # o contador adiciona 1 para o proximo numero 
    valor_int +=1 
    # Fim 
