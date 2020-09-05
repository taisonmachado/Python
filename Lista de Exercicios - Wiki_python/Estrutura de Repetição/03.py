#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

while True:
    nome = input("Seu nome: ")
    idade = int(input("Sua idade: "))
    salario = float(input("Seu Salário: "))
    sexo = input("Seu sexo: ").lower()
    est_civl = input("Estado civil: (s) solteiro (c) casado (v) viúvo(a) (d) divorciado\n").lower()
    
    if(len(nome)<3):
        print("erro no nome")
    elif(idade<0 and idade>150):
        print("erro na idade")
    elif(salario<0):
        print("erro no salario")
    elif(est_civl!="s" and est_civl!="c" and est_civl!="v" and est_civl!="d"):
        print("erro no estado civil")
    else:
        print("tudo certo")
        break