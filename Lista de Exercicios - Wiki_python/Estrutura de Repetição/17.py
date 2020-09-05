#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input("Digite um número: "))
fatorial = num
while(num>1):
    num-=1
    fatorial *= num
    
print("fatorial = %i" %fatorial)