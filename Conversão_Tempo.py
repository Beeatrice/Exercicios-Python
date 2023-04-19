# -*- coding: utf-8 -*-
# Programa: ConversãodeTempo.py
# Programadora: Beatriz Sanabria
# Data: 19/04/2023

# 1° Passo vamos criar uma variavel chamada segundos para guardar o valor inteiro que o usuario vai digitar.
segundos = int(input())
# 2° Passo  vamos somar que o valor de horas é segundos dividido inteiramente por 3600. 
horas = segundos // 3600
# 2.1° Passo vamos armazenar o valor de segundos com resto da divisão  de 3600.
segundos %= 3600
# 2.2° Passo  vamos somar que o valor de minutos é segundos dividido inteiramente por 60.
minutos = segundos // 60
# 2.3° Passo vamos armazenar o valor de segundos com resto da divisão de 60.
segundos %= 60
# 3° Passo vamos retornar horas, minutos, e segundos do valor do usuario.
print("{}:{}:{}".format(horas, minutos, segundos))
# Fim.
