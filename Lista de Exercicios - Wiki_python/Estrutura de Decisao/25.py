#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação 
#da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada 
#como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, 
#ele será classificado como "Inocente".

cont = 0
print("caso concorde com as perguntas, responda com um S")
resposta = input("Telefonou para a vítima?").lower()
if(resposta=="s"):
    cont+= 1
resposta = input("Esteve no local do crime?").lower()
if(resposta=="s"):
    cont+= 1
resposta = input("Mora perto da vítima?").lower()
if(resposta=="s"):
    cont+= 1
resposta = input("Devia para a vítima?").lower()
if(resposta=="s"):
    cont+= 1
resposta = input("Já trabalhou com a vítima?").lower()
if(resposta=="s"):
    cont+= 1
    
if(cont ==2):
    print("Suspeito")
elif(cont==3 or cont==4):
    print("Cúmplice")
elif(cont==5):
    print("Assassino")
else:
    print("Inocente")