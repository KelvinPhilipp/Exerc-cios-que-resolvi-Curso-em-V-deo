#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A"; Em que posição ela aparece a primeira vez; em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip().upper()
q = len(frase)



print(f'A frase possui {q} caracteres')
print(f'A letra A aparece {frase.count('A')} vezes na frase\nA primeira letra A aparece na posição {frase.find('A')+1}\nA última letra A aparece na posição {(frase.rfind('A')+1)}')