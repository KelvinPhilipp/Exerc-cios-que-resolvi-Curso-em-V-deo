#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200 Km e R$ 0,45 para viagens mais longas

distancia_viagem = float(input('Digite a distância do percurso que irá realizar na sua viagem: '))

if distancia_viagem > 200:
    valor = distancia_viagem * 0.45
    print(f'O valor da viagem será de R$ {valor}')

else:
    valor = distancia_viagem * 0.5
    print(f'O valor da viagem será de R$ {valor}')