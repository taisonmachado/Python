# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

raio = int(input("Digite o raio do círculo: "))
area = math.pow(raio, 2) * math.pi

print("Area: ", area)

input("Pressione Enter para continuar")