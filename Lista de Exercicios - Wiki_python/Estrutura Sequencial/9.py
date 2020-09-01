# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a 
# temperatura em graus Celsius.
#    C = 5 * ((F-32) / 9).

fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit-32) / 9)

print("Temperatura em Celsius: ", celsius)

input("Pressione Enter para continuar")