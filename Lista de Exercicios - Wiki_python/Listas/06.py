#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
#imprima o número de alunos com média maior ou igual a 7.0.

lista_notas = []
aprovados = 0
for aluno in range(10):
    media = 0
    print("Aluno %i" %(aluno+1))
    for nota in range(4):
        media += float(input("Nota %i = " %(nota+1)))
    media = media/4
    lista_notas.append(media)
    if(media>=7):
        aprovados+=1
        
print("Notas: ", lista_notas)
print("Quantidade de aprovado(s): ", aprovados)