#Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar 
#se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
#e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

num_pessoas = int(input("Quantas pessoas serão entrevistadas? "))

respostas = []
for i in range(num_pessoas):
    respostas.append(int(input("Qual a sua idade? ")))
    
media = 0
for idade in respostas:
    media += idade

media = media/(len(respostas))

if media>=0 and media<=25:
    print("Turma Jovem")
elif media>=26 and media<=60:
    print("Turma Adulta")
else:
    print("Turma Idosa")