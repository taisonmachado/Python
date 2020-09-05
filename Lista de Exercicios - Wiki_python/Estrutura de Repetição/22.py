#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, 
#por quais números ele é divisível.

num = int(input("Digite um número: "))

divisores = 0
lista_div = []
for i in range(1, num+1):
    if num%i == 0:
        divisores += 1
        lista_div.append(i)

if(divisores==2):
    print("é primo")
else:
    print("não é primo")
    print("é divisível por: ")
    for i in lista_div:
        print(i, end=" ")