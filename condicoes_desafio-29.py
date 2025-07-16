#Escreva um programa que leia a velocidade a velocidade de um carro. Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade_carro = float(input("O velocímetro registrou a velocidade de: "))
limite_velocidade = 80
multa = (velocidade_carro - limite_velocidade) * 7

if velocidade_carro > limite_velocidade:
    print(f'Você ultrapassou o limite de velocidade permitido nesta via, atingindo {velocidade_carro} km/h e portanto será multado em R$ {multa}')
else:
    print('Motorista dentro do limite de velocidade estabelecido')            