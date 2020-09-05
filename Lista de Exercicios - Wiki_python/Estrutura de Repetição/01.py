#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

while True:
    num = int(input("Digite um número de 0 a 10: "))
    if(num>=0 and num<=10):
        print("Número válido!")
        break
    print("Número Inválido\n")