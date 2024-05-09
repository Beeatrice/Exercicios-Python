# Lendo a data no formato dd/mm/aaaa
data = input()

# Dividindo a data em dia, mês e ano
dia, mes, ano = map(int, data.split('/'))

# Verificando se o ano é bissexto
bissexto = ((ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0))

# Definindo o número de dias em cada mês
dias_mes = {
    1: 31,  # janeiro
    2: 29 if bissexto else 28,  # fevereiro
    3: 31,  # março
    4: 30,  # abril
    5: 31,  # maio
    6: 30,  # junho
    7: 31,  # julho
    8: 31,  # agosto
    9: 30,  # setembro
    10: 31,  # outubro
    11: 30,  # novembro
    12: 31   # dezembro
}

# Verificando se o dia é o último do mês
if dia == dias_mes[mes]:
    dia = 1
    mes += 1
    if mes > 12:
        mes = 1
        ano += 1
else:
    dia += 1

# Imprimindo a data do dia seguinte
print(f"{dia:02d}/{mes:02d}/{ano}")
