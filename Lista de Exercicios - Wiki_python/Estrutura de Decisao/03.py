#Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite o sexo: (F) ou (M) ")

if(sexo == 'M' or sexo == 'm'):
    print("Sexo Masculino")
elif(sexo == 'F' or sexo =='f'):
    print("Sexo Feminino")
else:
    print("Sexo invalido")