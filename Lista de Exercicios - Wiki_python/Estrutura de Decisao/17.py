#Faça um Programa que peça um número correspondente a um determinado ano e em seguida 
#informe se este ano é ou não bissexto.

ano = int(input("informe um ano: "))

if(ano%4 == 0):
    print("é bissexto")
else:
    print("nao é bissexto")