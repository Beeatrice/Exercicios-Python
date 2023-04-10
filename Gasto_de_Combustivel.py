# -*- coding: utf-8 -*-
# Programa: 1017-gastodecombustivelpy LISTA
# Programadora: Beatriz Sanabria
# Data: 26/04/2023

# 1° Passo. Vamos ler as duas variaveis que o usuario vai digitar, cada uma em uma linha e numeros inteiros.
tempo = int(input())
velocidade = int(input())
# 2° Passo. Vamos calcular a distancia que o carro vai anda para ver quantos litros de conbustivel ira gastar, então distacia é tempo que é a primeira variavel digitada pelo usuario vezes a valocidade que é a segunda variavel.
distancia = tempo * velocidade
# 2.1° Passo. Vamos calcular os litros gastos pegando o valor da distancia divida por 12 que é o KM que o carro do joãozinho faz por litro. 
litros = distancia/12
# 3° Passo. Vamos retornar os litros gastos por KM (distancia) que o usuario deseja saber 
print("{:.3f}".format(litros))
# Fim. Me corrija se estiver errado professor
