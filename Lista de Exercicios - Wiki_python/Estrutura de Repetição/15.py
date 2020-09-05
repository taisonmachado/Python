#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
#Faça um programa capaz de gerar a série até o n−ésimo termo.

x = int(input("Quantos termos deve ter a série? "))

anterior = 0
atual = 1
for i in range(x):
    print(atual, end=" ")
    aux = atual
    atual += anterior
    anterior = aux