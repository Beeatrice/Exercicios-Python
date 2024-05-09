# -*- coding: utf-8 -*-
# Programa: mostrames.py
# Programador: Beatriz
# Data: 09/05/2024
# Este Programa ilustra a passagem de uma string como refência.
# O programa lê um número entre um e 12 e usando uma função 
# def mostrames(mes)
# computa o mês (Janeiro a Dezembro) referente ao valor lido,
# retorna o mês para a função principal que imprime o resultado.
# funções
def mostrames(mes):
    # Lista com os nomes dos meses
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    # Verifica se o número do mês está dentro do intervalo válido
    if 1 <= mes <= 12:
        # Retorna o nome do mês correspondente
        return meses[mes - 1]
    else:
        # Retorna 'Número inválido' se o número do mês estiver fora do intervalo
        return 'Número inválido'

# início
# Passo 1. Leia o número do mês    
mes = int(input())
# Passo 2. Compute o mês equivalente
nome = mostrames(mes)
# Passo 3. Imprima o mês equivalente
print(nome)
# fim do módulo principal
