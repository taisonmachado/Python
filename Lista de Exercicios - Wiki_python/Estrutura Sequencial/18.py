#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arq = float(input("Digite o tamanho do arquivo em MB: "))
vel_internet = float(input("Digite a velocidade  da internet em Mbps: "))

tempo_download_minuto= int((tamanho_arq/vel_internet)/60)
tempo_download_segundo = int((tamanho_arq/vel_internet)%60)


print("O download durará", tempo_download_minuto, "m e", tempo_download_segundo, "s")

input("\nPressione Enter para continuar")