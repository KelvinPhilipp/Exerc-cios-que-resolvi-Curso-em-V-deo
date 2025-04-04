#Crie um programa que leia o nome completo de uma pessoa e mostre: O nome com todas as letras maiúsculas; O nome com todas as letras minúsculas; Quantas letras ao todo (sem considerar espaços) a string possui; Quantas letras tem o primeiro nome.

nome = input('Digite o seu nome completo: ')
letras = nome.split()
jun = ''.join(letras)

print(f'O nome {nome}, \nEm maíusculo é impresso da forma {nome.upper()}, \nem minúsculo é impresso da forma {nome.lower()} \ne contém {len(jun)} letras\nSeu primeiro nome é: {letras[0]} e contém {len(letras[0])} letras')
