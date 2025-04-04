#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip().title().split()
p = nome[0]
u = nome[-1]

print(f'O seu primeiro nome é: {p}\nO seu ultimo nome é: {u}')



