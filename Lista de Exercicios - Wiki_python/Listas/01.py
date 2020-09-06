#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

vetor = []

i = 0
while i < 5:
    vetor.append(int(input("Digite um número: ")))
    i+=1
    
for num in vetor:
    print(num, end=" ")