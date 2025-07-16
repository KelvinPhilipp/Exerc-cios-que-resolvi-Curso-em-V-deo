#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 > numero2 and numero2 < numero3:
    print(f'O número maior é o: {numero1}\nO número menor é o: {numero2}')

elif numero1 > numero2 and numero2 > numero3:
    print(f'O número maior é o: {numero1}\nO número menor é o: {numero3}')

elif numero3 > numero2 and numero2 > numero1:
    print(f'O número maior é o: {numero3}\nO número menor é o: {numero1}')

elif numero3 > numero2 and numero2 < numero1:
    print(f'O número maior é o: {numero3}\nO número menor é o {numero2}')

elif numero2 > numero1 and numero1 > numero3:
    print(f'O número maior é o: {numero2}\nO número menor é o: {numero3}')

else:
    print(f'O número maior é o: {numero2}\nO número menor é o: {numero1}')