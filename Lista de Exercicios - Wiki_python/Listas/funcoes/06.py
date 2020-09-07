#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
#Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
#Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
#Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 
#Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. 
#Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def imprime_hora(hora, minuto, aux):
    print("%i:%i %s.M" %(hora, minuto, aux))

def converte_horas(hora, minuto):
    if(hora>12):
        hora -= 12
        imprime_hora(hora, minuto, "P")
    else:
        imprime_hora(hora, minuto, "A")
        

print("Digite -1 na hora para encerrar")
while True:
    hora = int(input("Hora: "))
    if hora<0:
        break
    minuto = int(input("Minuto: "))
    converte_horas(hora, minuto)