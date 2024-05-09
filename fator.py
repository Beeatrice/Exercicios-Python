# Programador: Beatriz
# Data: 09/05/2024

#Este código lê um número inteiro da entrada, calcula o maior fator desse número e imprime ambos. 
#Se o número for 0 ou 1, o maior fator será o próprio número. Caso contrário, ele itera de 2 até um número anterior ao número fornecido, 
#verificando se é um divisor do número fornecido e atualizando o maior fator encontrado.

def main():
    # Lendo o número inteiro
    numero = abs(int(input()))

    # Calculando o maior fator
    max_fator = 1
    for i in range(2, numero):
        if numero % i == 0:
            max_fator = i

    # Imprimindo o número e o seu maior fator
    print(numero, max_fator)

if __name__ == "__main__":
    main()
