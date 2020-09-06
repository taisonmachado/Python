#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caracteres = []
consoantes = []

print("Digite 10 caracteres: ")
for i in range(10):
    caracteres.append(input())
    c = caracteres[i]
    if(c != "a" and c != "e" and c != "i" and c != "o" and c != "u"):
        consoantes.append(c)
    
print("Foi digitado %i consoantes." %len(consoantes))
print("consoantes:", end=" ")
for c in consoantes:
    print(c, end=" ")