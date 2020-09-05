#Faça um programa que leia 5 números e informe a soma e a média dos números.

media = 0
print("Informe 5 números: ")
for i in range(5):
    num = int(input(""))
    media += num
        
print("A média é %.2f" %(media/5))