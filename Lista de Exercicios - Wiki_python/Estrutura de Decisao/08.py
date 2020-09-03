#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
# sabendo que a decisão é sempre pelo mais barato.

lista = []
lista.append(float(input("Digite o preço do produto 1: ")))
lista.append(float(input("Digite o preço do produto 2: ")))
lista.append(float(input("Digite o preço do produto 3: ")))

print("O Produto", lista.index(min(lista))+1, "é o mais barato")