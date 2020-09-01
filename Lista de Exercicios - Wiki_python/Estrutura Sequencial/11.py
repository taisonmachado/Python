# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

inteiro1 = int(input("Digite um numero inteiro: "))
inteiro2 = int(input("Digite mais um numero inteiro: "))
real = float(input("Agora digite um número real: "))

print("o produto do dobro do primeiro com metade do segundo: ", (2*inteiro1)*(inteiro2/2))
print("a soma do triplo do primeiro com o terceiro: ", (3*inteiro1)+ real)
print("o terceiro elevado ao cubo: ", real**3)

input("Pressione Enter para continuar")