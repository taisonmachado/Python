#Faça um Programa que leia três números e mostre o maior e o menor deles.

lista = []
lista.append(float(input("Digite 3 números:\n")))
lista.append(float(input()))
lista.append(float(input()))

print("O maior é o", max(lista))
print("O menor é o", min(lista))