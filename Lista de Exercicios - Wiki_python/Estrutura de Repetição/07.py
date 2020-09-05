#Faça um programa que leia 5 números e informe o maior número.

maior = 0
print("Informe 5 números: ")
for i in range(5):
    num = int(input(""))
    if(num > maior):
        maior = num
        
print("O maior é %i" %maior)