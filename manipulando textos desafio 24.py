#Crie um programa que leia o nome de uma cidade de diga se ela começa ou não com o nome Santo


cidade = str(input('Digite o nome da cidade em que nasceu: ')).strip()
m = cidade.upper()
m = m.split()


if 'SANTO' in m [0]:
    print('Sua cidade de origem, começa com o nome Santo')
else:
    print('Sua cidade de origem, não começa com o nome Santo')