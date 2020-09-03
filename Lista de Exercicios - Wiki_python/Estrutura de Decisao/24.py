#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

import math

num1 = float(input("Digite dois números: "))
num2 = float(input())

print("Qual operação deseja realizar:")
print("(a) adição")
print("(s) subtração")
print("(m) multiplicação")
print("(d) divisão")

operacao = input().lower()

if(operacao == "a"):
    resultado = num1+num2
elif(operacao == "s"):
    resultado = num1-num2
elif(operacao == "m"):
    resultado = num1*num2
elif(operacao == "d"):
    resultado = num1/num2
else:
    print("erro")

print("=", resultado)
if((resultado%2)==0):
    print("Número par")
else:
    print("Número impar")

if(resultado>0):
    print("Número positivo")
else:
    print("Número negativo")

if(math.ceil(resultado) == resultado):
    print("Número Inteiro")
else:
    print("Número Decimal")