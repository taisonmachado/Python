#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input("Digite um número: "))

if(num == 0):
    print("Número nulo")
elif(num>0):
    print("Número positivo")
else:
    print("Número negativo")