# -*- coding: utf-8 -*-
# Programa: medianotas4.py
# Programador: Beatriz Sanabria
# Data: 30/03/2024


# Entrada dos dados
numero_estudante = input().strip()

# Notas das provas
notas_provas = [float(input().strip()) for _ in range(3)]

# Notas dos trabalhos
notas_trabalhos = [float(input().strip()) for _ in range(2)]

# Frequência do estudante
frequencia = int(input().strip())

# Prova optativa
fez_prova_optativa = input().strip().upper()
nota_prova_optativa = 0.0
if fez_prova_optativa == 'S':
    nota_prova_optativa = float(input().strip())

# Cálculo da média das provas
media_provas = sum(notas_provas) / len(notas_provas)

# Cálculo da média dos trabalhos
media_trabalhos = sum(notas_trabalhos) / len(notas_trabalhos)

# Se o aluno fez a prova optativa, substitui a menor nota das provas pela nota da prova optativa
if fez_prova_optativa == 'S':
    menor_nota = min(notas_provas)
    indice_menor_nota = notas_provas.index(menor_nota)
    notas_provas[indice_menor_nota] = nota_prova_optativa

# Cálculo da média final
media_final = round(0.75 * sum(notas_provas) / len(notas_provas) + 0.25 * media_trabalhos, 1)

# Verificação da situação do aluno
situacao_aluno = ""
if media_final >= 6.0 and frequencia >= 75:
    situacao_aluno = "AP"
elif media_final < 6.0 and frequencia >= 75:
    situacao_aluno = "RN"
else:
    situacao_aluno = "RF"

# Saída
print(f"{numero_estudante}: Média = {media_final:.1f}, Frequência = {frequencia}% - {situacao_aluno}")



# pós: menorNota == min{prova1, prova2, prova3} and
#      ((mediaFinal == 0.75*(prova1+prova2+prova3)/3.0 + 
#      0.25*(trab1+trab2)/2.0) or
#      (mediaFinal == 0.75*(prova1+prova2+prova3-menorNota+opt)/3.0
#      + 0.25*(trab1+trab2)/2.0)) and ((mediaFinal >=6.0 and 
#      freq >= 75 and 'AP') or (mediaFinal < 6.0 
#      and freq >= 75 and 'RN') or (freq < 75 and 'RF'))
# fim do módulo principal
