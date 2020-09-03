#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
#porém não há limites para a quantidade de carne por cliente. 
#Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
#contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
#valor do desconto e valor a pagar.

print("#                      Até 5 Kg           Acima de 5 Kg -    Código")
print("#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg -         1")
print("#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg -         2")
print("#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg -         3\n")

tipo_carne = int(input("Digite o código da carne que deseja: "))
kg = float(input("Quantos quilos deseja? "))
cartao_sn = input("Deseja pagar com cartao Tabajara? (S)Sim (S)Não -> ").lower()

if(tipo_carne<1 or tipo_carne>3):
    print("ERRO")
else:
    print("\nCUPOM FISCAL:")
    print("Peso: %.2f kg" %kg)
    
    if(tipo_carne == 1):
        print("Carne: File Duplo")
        if(kg>5):
            total = kg*5.8
        else:
            total = kg*4.9
    elif(tipo_carne==2):
        print("Carne: Alcatra")
        if(kg>5):
            total = kg*6.8
        else:
            total = kg*5.9
            
    elif(tipo_carne == 3):
        print("Carne: Picanha")
        if(kg>5):
            total = kg*7.8
        else:
            total = kg*6.9
    
    print("PREÇO TOTAL: R$%.2f" %total)    
    
    if(cartao_sn == "s"):
        desconto = total*0.05
        print("Pagamento: Cartão Tabajara")
    else:
        desconto = 0
        print("Pagamento: Dinheiro")
    
    print("Desconto: -R$%.2f" %desconto)
    print("Valor pago: R$%.2f" %(total-desconto))
