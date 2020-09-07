#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de 
#mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def mes_extenso(data):
  meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
  aux = data.split("/")
  dia = int(aux[0])
  mes = int(aux[1])
  ano = int(aux[2])
  if dia < 0 or dia > 31 or mes < 0 or mes > 12 or ano < 0:
    return "Data Inválida"
  else:
    return "%i de %s de %i" %(dia, meses[mes-1], ano)

print(mes_extenso("06/09/2020"))