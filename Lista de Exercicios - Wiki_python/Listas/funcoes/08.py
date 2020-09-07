#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def num_digitos(num):
  num = str(num)
  return len(num)

print(num_digitos(123))