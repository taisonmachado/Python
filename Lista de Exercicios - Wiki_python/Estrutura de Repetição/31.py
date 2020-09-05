#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
#Faça um programa que implemente uma caixa registradora rudimentar.
#O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
#Um valor zero deve ser informado pelo operador para indicar o final da compra. 
#O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
#para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, 
#para registrar a próxima compra. 

i = 1
valor_prod = 1
lista_prod = []
while(valor_prod > 0):
    valor_prod = float(input("Valor do Produto %i = " %i))
    lista_prod.append(valor_prod)
    i+=1

valor_pago = float(input("Cliente pagou = "))
print("\n\nLOJAS TABAJARA\n")
i = 1
total = 0
for prod in lista_prod:
    print("Produto %i: R$%.2f" %(i, prod))
    i+=1
    total += prod
    
print("Total: R$%.2f" %total)
print("Dinheiro: R$%.2f" %valor_pago)
print("Troco: R$%.2f" %(valor_pago-total))