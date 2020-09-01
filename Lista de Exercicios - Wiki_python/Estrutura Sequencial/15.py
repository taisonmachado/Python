# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

horas_trabalhadas = int(input("Quantas horas você trabalhou no mês: "))
salario_hora = float(input("Quanto você ganha por hora trabalhada: "))

salario_bruto = horas_trabalhadas*salario_hora
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05

print("\n+ Salário Bruto: R$", salario_bruto)
print("- IR (11%): R$", ir)
print("- INSS (8%): R$", inss)
print("- Sindicato (5%): R$", sindicato)
print("= Salário Líquido: R$", salario_bruto - ir - inss - sindicato)

input("\nPressione Enter para continuar")