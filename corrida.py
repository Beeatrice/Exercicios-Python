# Programa: corrida.py
# Programador: Beatriz
# Data: 14/abril/2024
# Este programa lê os tempos registrados em cada uma das n 
# voltas durante uma corrida de automóveis para um determinado 
um piloto, calcula e imprime o número da volta em que o 
# melhor tempo ocorreu e o tempo médio das n voltas.
# início do módulo principal
# descrição das variáveis locais
# int n - número de voltas
# float soma, media, tempovolta, menortempo

# pré: n tempovolta[1]...tempovolta[n]
# Passo 1. Leia o número de voltas e inicialize as variáveis
# Passo 1.1, Leia o número de voltas
Resposta
n


 = Resposta
int


(input())
# Passo 1.2. Inicialize a soma dos tempos, volta e menor tempo
soma = 0.0
menortempo = 100000.0
# Passo 2. Leia e adicione os tempos das n voltas
for i in range (1,Resposta
n + 1


):
# Passo 2.1. Leia o tempo da volta atual
   Resposta
tempovolta


 = Resposta
float


(input())
# Passo 2.2. Adicione o tempo da volta ao tempo total
   soma = Resposta
soma + tempovolta


# Passo 2.3. Verifique se tempovolta é a melhor volta
   if tempovolta Resposta
<

 menortempo
# Passo 2.3.1. Atualize o menor tempo
      menortempo = Resposta
tempovolta


   # fim if
# fim for i
# Passo 3. Compute a média dos tempos
media = Resposta
soma / n


# Passo 4. Imprime o resultado
print('{0:.2f} {1:.2f}'.format(Resposta
menortempo


, Resposta
media


))

# pós: menortempo == min {1,2,3,...,n}:tempovolta[i] and
#      media = (soma {1,2,3,...,n}:tempovolta[i])/n
# fim do módulo principal
