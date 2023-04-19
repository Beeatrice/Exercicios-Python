# -*- coding: utf-8 -*-
# Programa: 1020-Idade_em_dias.py
# Programadora: Beatriz Sanabria
# Data: 19/04/2023

# 1° Passo. Vamos armazenar na variavel diasvividos o numero que o usuario digitar.
diasvividos = int(input())
# 2° Passo. Vamos fazer a divisão inteira para trasformar o valor de diasvividos em anos, usando divisão inteira e resto da divisão.
anos = diasvividos // 365
diasvividos = diasvividos % 365
# 2.1° Passo. Vamos fazer a divisão inteira para trasformar o valor de diasvividos em meses, usando divisão inteira e resto da divisão.
meses = diasvividos // 30
diasvividos = diasvividos % 30
# 2.2° Passo. Vamos fazer a divisão inteira para trasformar o valor de diasvividos em dias, usando divisão inteira e resto da divisão.
dias = diasvividos // 365
dias = diasvividos % 365
# 3° Passo. Vamos retornar os anos, meses, e dias que equivalem o numero que o usuario digitou.
print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
# Fim.
