#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
#O usuário deve informar de qual numero ele deseja ver a tabuada. 

num = int(input("Deseja ver a tabuada de qual número? "))

for i in range(1,11):
    print("%i x %i = %i" %(num, i, num*i))