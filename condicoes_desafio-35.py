#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

primeira_reta = float(input('Digite o comprimento: '))
segunda_reta = float(input('Digite o comprimento: '))
terceira_reta = float(input('Digite o comprimento: '))

if primeira_reta > segunda_reta and segunda_reta > terceira_reta and segunda_reta + terceira_reta >= primeira_reta:
     print('Com as medidas fornecidas é possível formar um triângulo.')
    
elif primeira_reta > terceira_reta and terceira_reta > segunda_reta and segunda_reta + terceira_reta >= primeira_reta:
     print('Com as medidas fornecidas é possível formar um triângulo.')

elif segunda_reta > primeira_reta and primeira_reta > terceira_reta and primeira_reta + terceira_reta >= segunda_reta:
     print('Com as medidas fornecidas é possível formar um triângulo.')

elif segunda_reta > terceira_reta and terceira_reta > primeira_reta and primeira_reta + terceira_reta >= segunda_reta:
     print('Com as medidas fornecidas é possível formar um triângulo.')

elif terceira_reta > primeira_reta and primeira_reta > segunda_reta and primeira_reta + segunda_reta >= terceira_reta:
     print('Com as medidas fornecidas é possível formar um triângulo.')

elif terceira_reta > segunda_reta and segunda_reta > primeira_reta and primeira_reta + segunda_reta >= terceira_reta:
      print('Com as medidas fornecidas é possível formar um triângulo.')
else:
     print('Não é possível formar um triângulo com as medidas fornecidas.')
