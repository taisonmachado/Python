#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
#dezenas e unidades do mesmo.
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 
#111, 25, 20, 10, 21, 11, 1, 7 e 16)

numero = int(input("Digite um número menor que 1000: "))

if(numero >= 1000 or numero <=0):
    print("numero invalido")
else:
    unidade = numero%10
    numAux = (numero-unidade)/10
    dezena = numAux%10
    numAux = (numAux-dezena)/10
    centena = numAux%10
    
    print("%i centena(s), %i dezena(s) e %i unidade(s)" %(centena, dezena, unidade))