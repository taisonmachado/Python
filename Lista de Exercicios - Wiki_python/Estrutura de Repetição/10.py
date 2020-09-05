#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no 
#intervalo compreendido por eles.

print("Informe dois números: ")
num1 = int(input())
num2 = int(input())

print("\nIntervalo entre os dois números: ")
for i in range(num1+1, num2):
    print(i)