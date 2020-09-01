#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_quadrado = int(input("Digite o comprimento da lateral do quadrado em cm: "))
area = lado_quadrado*lado_quadrado

print("Area do quadrado: ", area, "cm")
print("Dobro da area: ", area*2, "cm")

input("Pressione Enter para continuar")