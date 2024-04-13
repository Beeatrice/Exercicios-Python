#Programadora: Beatriz Sanabria
#Uma string é denominada palíndromo quando ela lida do início para o final tem o mesmo significado se a ordem dos caracteres é lida do final para o início. Por exemplo:
#MADAM
#463364
#ABLE WAS I ERE I SAW ELBA
#são palíndromos.
#Projete e implemente um programa para ler uma string de caracteres e então determinar se ela é um palíndromo. Caracteres maiúsculos e minúsculos de um mesmo símbolo são considerados iguais. A string pode ter caracteres espaço.A entrada é dada por por um fluxo numa linha contente caracteres do alfabeto latino e o caractere espaço. As strings não possuem dois caracteres espaço juntos. A saída consiste em imprimir para a string da entrada a mensagem se ela é palíndromo ou não.
#Neste exercício não pode ser usado nenhuma função ou módulo para manipular blocos da string nem slicing. Só pode ser utilizado a manipulação e concatenação de 'caracteres' e comparação de strings. Podem ser utilizados os métodos string.upper() e string.lower().

# Ler a string da entrada
entrada = input()

# Converter a string para letras minúsculas (ou maiúsculas, tanto faz)
entrada = entrada.lower()

# Inicializar a string inversa
inversa = ""

# Construir a string inversa
for i in range(len(entrada) - 1, -1, -1):
    inversa += entrada[i]

# Verificar se a string original é igual à inversa
if entrada == inversa:
    print("palíndromo")
else:
    print("não palíndromo")
