# -*- coding: utf-8 -*-
# Programa: producao.py
# Programador: Beatriz SAnabria
# Data: 12/05/2024
# Este programa le a produção semanal de álcool de uma dada usina e
# calcula e imprime a soma da produção da semana.

# Lê a produção diária de álcool em uma semana
producao_semana = list(map(float, input().split()))

# Calcula a produção total da semana
producao_total = sum(producao_semana)

# Imprime a produção total da semana
print("{:.2f}".format(producao_total))
