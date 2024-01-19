#Para unir duas listas podemos simplesmente utilizar o símbolo de +:
lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000, 20000, 50000]

lojas.sort()
vendas.sort()

print(lojas+vendas)
['Curitiba', 'Rio de Janeiro', 'São Paulo', 10000, 20000, 50000]
#Não é o que queremos. Vamos tentar inverter a ordem:

print(lojas+vendas)
['Curitiba', 'Rio de Janeiro', 'São Paulo', 10000, 20000, 50000]
#Ainda não é o que queremos. Neste caso unir as listas com o símbolo de + não atende a nossa necessidade, pois queremos relacionar o nome ao valor!

#Já estamos quase finalizando, agora vamos a uma parte importante: utilizar um Tupla para unir listas e conseguir relacionar o nome ao valor.
