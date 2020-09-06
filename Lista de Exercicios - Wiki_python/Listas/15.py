#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando 
#a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
#Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;

vetor = []
soma = 0
print("Digite -1 quando quiser encerrar")
while True:
    num = int(input())
    if num==-1:
        break
    else:
        vetor.append(num)
        soma += num
        
qtd = len(vetor)
media = soma/qtd
abaixo7 = 0
acima_media = 0

for i in vetor:
    if i > media:
        acima_media +=1
    if i < 7:
        abaixo7 += 1
        
print("Quantidade de valores = %i" %qtd)
print("Vetor = ", vetor)
vetor.reverse()
print("Vetor inverso: ")
for i in vetor: 
    print(i)
    
print("Soma dos valores = ", soma)
print("Média dos valores = ", media)
print("Valores acima da média = ", acima_media)
print("Valores abaixo de 7 = ", abaixo7)
print("05092020")