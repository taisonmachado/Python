#Faça um Programa que peça os 3 lados de um triângulo. 
#O programa deverá informar se os valores podem ser um triângulo. 
#Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Informe os 3 lados do triângulo: "))
lado2 = float(input())
lado3 = float(input())

if(lado1+lado2 > lado3 or lado1+lado3>lado2 or lado2+lado3>lado1):
    print("É um triângulo ", end="")
    
    if(lado1==lado2 and lado2==lado3):
        print("equilátero")
    elif(lado1==lado2 or lado2==lado3 or lado1==lado3):
        print("isósceles")
    else:
        print("escaleno")
else:
    print("nao é um triângulo")