# Programa: corrida.py
# Programador:
# Data: 27/06/2012
# Este programa lê os tempos registrados em cada uma das n 
# voltas durante uma corrida de automóveis para um determinado piloto,
# calcula e imprime o número da volta em que o melhor tempo ocorreu 
# e o tempo médio das n voltas.
# início do módulo principal
# descrição das variáveis locais
# int n - número de voltas
# float soma, media, tempovolta, menortempo

# pré: n tempovolta[1]...tempovolta[n]

# Passo 1. Leia o número de voltas e inicialize as variáveis
# Passo 1.1, Leia o número de voltas
n = int(input())

# Passo 1.2. Inicialize a soma dos tempos, volta e menor tempo
soma = 0.0
menortempo = 100000.0
melhor_volta = 0  # Armazena o número da volta com o melhor tempo

# Passo 2. Leia e adicione os tempos das n voltas
for i in range(1, n + 1):
    # Passo 2.1. Leia o tempo da volta atual
    tempovolta = float(input())
    
    # Passo 2.2. Adicione o tempo da volta ao tempo total
    soma += tempovolta

    # Passo 2.3. Verifique se tempovolta é a melhor volta
    if tempovolta < menortempo:
        # Passo 2.3.1. Atualize o menor tempo
        menortempo = tempovolta
        melhor_volta = i  # Armazena o número da volta com o melhor tempo
    # fim if
# fim for i

# Passo 3. Compute a média dos tempos
media = soma / n

# Passo 4. Imprime o resultado
print(f'{melhor_volta} {menortempo:.2f} {media:.2f}')

# pós: menortempo == min {1,2,3,...,n}:tempovolta[i] and
#      media = (soma {1,2,3,...,n}:tempovolta[i])/n
# fim do módulo principal
