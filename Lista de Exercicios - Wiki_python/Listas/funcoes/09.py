#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverte(num):
  num = str(num)
  j = len(num)
  invertido = ""
  for i in range(j):
    invertido += num[j-1]
    j -=1
  return int(invertido)

print(reverte(123))