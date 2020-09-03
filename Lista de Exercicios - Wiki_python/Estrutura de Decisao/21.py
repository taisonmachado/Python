#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e 
#depois informar quantas notas de cada valor serão fornecidas. 
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
#O valor mínimo é de 10 reais e o máximo de 600 reais. 
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, 
#uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
#uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print("NOTAS DISPONÍVEIS : 100, 50, 10, 5, 1")
valor = int(input("Valor do saque(R$10~600):"))

if(valor<10 or valor >600):
    print("saque inválido")
else:
    nota100 = int(valor/100)
    valor = valor%100
    nota50 = int(valor/50)
    valor = valor%50
    nota10 = int(valor/10)
    valor = valor%10
    nota5 = int(valor/5)
    valor = valor%5
    nota1 = int(valor)
    print("Notas de R$100:", nota100)
    print("Notas de R$50:", nota50)
    print("Notas de R$10:", nota10)
    print("Notas de R$5:", nota5)
    print("Notas de R$1:", nota1)