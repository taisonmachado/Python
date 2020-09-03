#Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

import math

num = float(input("Digite um número: "))

if(math.ceil(num) == num):
    print("Número Inteiro")
else:
    print("Número Decimal")