#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

mensagem = input("Digite M-Matutino, V-Vespertino ou N-Noturno: ").lower()

if(mensagem == "m" or mensagem =="matutino"):
    print("Bom dia!")
elif(mensagem == "v" or mensagem =="vespertino"):
    print("Boa tarde!")
elif(mensagem == "n" or mensagem =="noturno"):
    print("Boa Noite!")
else:
    print("Valor Inválido")