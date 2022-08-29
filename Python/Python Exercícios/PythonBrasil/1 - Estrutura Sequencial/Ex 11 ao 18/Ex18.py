# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet
# (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def conversor():
    MB = float(input("Qual o tamanho do arquivo para download em MB? "))
    velMbps = float(input("Qual a velocidade para download em Mbps? "))
    
    tempo = round(((MB / velMbps) / 60), 2)
    
    print("O tempo em minutos é aproximadamente:", tempo)

conversor()

