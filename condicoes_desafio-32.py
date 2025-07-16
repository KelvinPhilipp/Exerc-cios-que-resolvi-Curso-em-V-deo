#Desenvolva um programa que leia um ano qualquer e mostre se ele é bissexto.
#regras para se definir se um ano e bissexto: Se for divisivel por 4, 100 e 400. Se divisivel por 4 e por 100, mas não por 400, ele não é bissexto.

ano = int(input('Digite o ano que deseja saber se é bissexto: '))

if ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('O ano consultado é bissexto')

elif ano % 4 == 0 and ano % 100 != 0:
    print('O ano consultado é bissexto')

else:
    print('O ano consultado não é bissexto')