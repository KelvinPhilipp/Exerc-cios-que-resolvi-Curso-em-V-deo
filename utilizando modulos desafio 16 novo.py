##Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
num=float(input('Digite um número qualquer: '))
print(f'O número {num} tem a parte inteira {math.trunc(num)}')
