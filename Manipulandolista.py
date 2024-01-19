lojas = ['Rio de Janeiro','São Paulo', 'Curitiba']
vendas = [10000, 20000, 50000]
#O .sort() ordena os valores do maior para o menor. Atenção: as duas listas não estão conectadas.

lojas.sort()
vendas.sort()
#Perceba que ao mudarmos a ordem, não temos mais a Rio de Janeiro -> 10000 / São Paulo -> 20000 / Curitiba -> 50000:

print(lojas)
print(vendas)
['Curitiba', 'Rio de Janeiro', 'São Paulo']
[10000, 20000, 50000]
