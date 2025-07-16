#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

numero_escolhido_jogador = int(input('Digite um número de 1 a 5: '))
numeros = [1, 2, 3, 4, 5]
numero_escolhido_computador = random.choice(numeros)

print(f'O número escolhido pelo jogador foi: {numero_escolhido_jogador}\nO número escolhido pelo computador foi: {numero_escolhido_computador}')

if numero_escolhido_jogador == numero_escolhido_computador:
    print('Parabéns, o jogador foi o vencedor! Os humanos continuam superiores!')

else:
    print('Infelizmente você perdeu para o computador, parece que a SKYNET ira dominar o mundo...')

