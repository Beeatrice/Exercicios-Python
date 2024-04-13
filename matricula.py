#Programadora: Beatriz Sanabria 
#As Coordenações de Curso da FACOM desejam saber quais alunos estão cursando simultaneamente Algoritmos e Programação I (API) e Introdução a Sistemas Digitais (ISD). As listas dos alunos matriculados em cada uma das disciplinas é dada pelo RGA (Registro Geral Acadêmico) dos alunos. Para simplificar, o RGA será dado por apenas 5 dígitos, sendo os dois primeiros dígitos indicando os dois últimos dígitos do ano de ingresso, o terceiro indica curso que o aluno está matriculado, e os dois últimos a ordem em que o aluno foi matriculado no curso. Não existem mais de 500 alunos cursando cada uma das disciplinas.
#Projete e implemente um programa que leia as duas listas das matrículas em API (ap1) e ISD (isd), e compute a interseção (ap1isd) das matrículas dos alunos nessas disciplinas. As matrículas de cada disciplina é dada por uma lista de inteiros com os números dos RGA´s dos estudantes na respectiva disciplina. A interseção também deve ser dada pela lista com os RGA´s dos alunos que estão matriculados em ambas as disciplinas. O seu programa programa deve ler um inteiro (tamap1), tamanho da lista que representa a disciplina API, a lista ap1 com os tamap1 RGA´s dos alunos matriculados na disciplina API, um inteiro tamisd, tamanho da lista da disciplina ISD, e a lista com os tamisd RGA´s dos alunos matriculados na disciplina ISD. O seu programa deve computar e imprimir a lista ap1isd, com a interseção das matriculas das disciplinas API e ISD. Caso não tenha nenhum aluno matriculado simultaneamente nas duas disciplinas, o programa deve imprimir uma lista vazia.
#A entrada é dada por 4 linhas. A primeira linha contém um inteiro tamap1 representando o tamanho da primeira lista. A segunda linha contém os tamap1 RGA´s de cada um dos alunos matriculados na disciplina API. A terceira linha contém um inteiro tamisd indicando o tamanho da segunda lista. A quarta linha contém os tamisd RGA´s de cada um dos alunos matriculados na disciplina ISD. A saída consiste em imprimir a lista dos RGA´s dos alunos que cursam simultaneamente as disciplinas API e ISD, seguindo a ordem em que eles aparecem na primeira lista. No caso da interseção ser vazia, imprima a lista vazia [].

#Ler as listas de matrículas em API e ISD
tamap1 = int(input())
ap1 = set(map(int, input().split()))

tamisd = int(input())
isd = set(map(int, input().split()))

# Calcular a interseção entre os conjuntos
ap1isd = ap1.intersection(isd)

# Imprimir a lista de RGA's dos alunos que cursam simultaneamente as disciplinas
print(list(ap1isd) if ap1isd else [])
