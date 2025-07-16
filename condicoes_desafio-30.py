#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

numero = int(input('Digite um número e eu lhe direi se ele é par ou ímpar: '))

if numero % 2 == 0:
    print('O número digitado é par')
else:
    print('O número digitado é ímpar')