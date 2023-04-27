# -*- coding: utf-8 -*-

def calcular_pontuacao(x, d):
    return x * d

# Função para determinar o vencedor de um jogo de dardos por distância
def determinar_vencedor(jogadas_joao, jogadas_maria):
    pontuacao_joao = sum([calcular_pontuacao(x, d) for x, d in jogadas_joao])
    pontuacao_maria = sum([calcular_pontuacao(x, d) for x, d in jogadas_maria])
    if pontuacao_joao > pontuacao_maria:
        return "JOAO"
    else:
        return "MARIA"

# Lendo o número de casos de teste
n = int(input())

# Iterando sobre cada caso de teste
for i in range(n):
    # Lendo as jogadas de João
    jogadas_joao = []
    for j in range(3):
        jogada = tuple(map(int, input().split()))
        jogadas_joao.append(jogada)
    
    # Lendo as jogadas de Maria
    jogadas_maria = []
    for j in range(3):
        jogada = tuple(map(int, input().split()))
        jogadas_maria.append(jogada)
    
    # Determinando o vencedor e imprimindo
    vencedor = determinar_vencedor(jogadas_joao, jogadas_maria)
    print(vencedor)
