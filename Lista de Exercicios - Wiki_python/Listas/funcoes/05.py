#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, 
#que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. 
#A função “altera” o valor de custo para incluir o imposto sobre vendas.

def soma_imposto(taxa_imposto, custo):
    taxa_imposto = taxa_imposto/100
    valor_final = custo + (taxa_imposto*custo)
    return valor_final
    
print(soma_imposto(50, 100)) #50% de imposto em um produto que vale 100 reais.