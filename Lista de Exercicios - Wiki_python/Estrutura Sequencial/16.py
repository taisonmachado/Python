# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
# cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
if(area%54>0):
    litro = int(area/3) + 1
    lata = int(litro/18) + 1
else:
    litro = int(area/3)
    lata = int(litro/18)

total = lata * 80
print("Você precisará comprar", lata, "lata (s) e o total ficará por: R$", total)

input("Pressione Enter para continuar")