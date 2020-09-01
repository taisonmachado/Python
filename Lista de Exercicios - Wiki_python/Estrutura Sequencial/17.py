# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados 
# da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

if((area%108)>0):
    litro = int(area/6) + 1
    lata = int(litro/18) + 1
    galao = int(litro/3.6) + 1
else:
    litro = int(area/6)
    galao = int(litro/3.6)
    lata = int(litro/18)

print("Você precisará comprar", lata, "latas e o total ficará por: R$", (lata*80))
print("Ou")
print("Comprar", galao, "galao (s) e o total ficará por: R$", (galao*25))

if(galao%5!=0 and galao>5):
    print("Ou, para economizar tinta,")
    print("Comprar", lata-1, "lata (s) e", galao%5, "galão (s) e o total ficará por: R$", ((lata-1)*80)+ (galao%5)*25)

input("\nPressione Enter para continuar")