#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.)

data = input("Digite uma data no formato dd/mm/aaaa: ")

data = data.split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

if(dia>0 and dia<=31 and mes>0 and mes<=12 and ano>0):
    print("Data válida")
else:
    print("Data inválida")