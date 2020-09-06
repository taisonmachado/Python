#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista_numeros = []
lista_par = []
lista_impar = []

print("Digite 20 números inteiros: ")
for i in range(20):
    lista_numeros.append(int(input()))
    num = lista_numeros[i]
    if num%2==0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print("Números: ", lista_numeros)
print("Par: ", lista_par)
print("Impar: ", lista_impar)