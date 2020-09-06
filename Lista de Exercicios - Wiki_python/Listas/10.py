#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_a = []
vetor_b = []
vetor_ab = []

print("Preencha o vetor A")
for i in range(10):
    vetor_a.append(input())
    
print("Preencha o vetor B")
for i in range(10):
    vetor_b.append(input())
    
for i in range(10):
    vetor_ab.append(vetor_a[i])
    vetor_ab.append(vetor_b[i])
    
print("Vetor A: ", vetor_a)
print("Vetor B: ", vetor_b)
print("Vetor A e B intercalados: ", vetor_ab)