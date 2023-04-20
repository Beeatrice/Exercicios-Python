# -*- coding: utf-8 -*-
# Programa: Aluguel_de_Carro.py 
# Programadora: Beatriz Sanabria
# Data: 20/04/2023

#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro
#alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o
#carrocusta R$60 por dia e R$0,15 por Km rodado.

dias_ultilizados = int(input('Digite a quantidade de dias usando o carro de aluguel:'))
km = float(input('Digite o Km rodada:'))
valor_total = (dias_ultilizados * 60) + (km * 0.15)
print('Total do valor a ser pago é R${:.2f}'.format(valor_total))
