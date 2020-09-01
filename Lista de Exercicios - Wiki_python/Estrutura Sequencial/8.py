# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

salario_hora = int(input("Quanto vc ganha por hora: "))
horas_mes = int(input("Quantas horas trabalhou no mês: "))

salario_total = salario_hora*horas_mes

print("Seu salário: R$", salario_total)

input("Pressione Enter para continuar")