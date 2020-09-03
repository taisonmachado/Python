#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o 
#FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
#O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações.

salarioHora = float(input("Digite quanto voce ganha por hora: "))
horasTrabalhadas = int(input("Digite quantas horas voce trabalhou: "))

salarioBruto = salarioHora*horasTrabalhadas

if(salarioBruto <= 900):
    i_renda = 0
elif(salarioBruto > 900 and salarioBruto <= 1500):
    i_renda = 0.05
elif(salarioBruto> 1500 and salarioBruto <=2500):
    i_renda = 0.1
else:
    i_renda= 0.2

sindicato = 0.03    
descontos = i_renda*salarioBruto + salarioBruto*sindicato
salarioLiquido = salarioBruto - descontos

print("Salário Bruto: R$", salarioBruto)
print("(-) Imposto de Renda (%.2f): R$%.2f" %(i_renda, i_renda*salarioBruto))
print("(-) Sindicato (%.2f): R$%.2f" %(sindicato ,salarioBruto*sindicato))
print("FGTS (%i): R$%.2f" %(11,salarioBruto*0.11))
print("Total de Descontos: R$%.2f" %descontos)
print("Salário Líquido: R$%.2f" %salarioLiquido)