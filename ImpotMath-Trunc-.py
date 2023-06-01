'''
Programa: ImpotMath-Trunc-.py
Programadora: Beatriz Sanabria
Data: 31/03/2023

Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira 
'''
# math.trunc() corta a parte inteira do número

import math
numero = float(input('Digite um numero: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(numero, math.trunc(numero)))

