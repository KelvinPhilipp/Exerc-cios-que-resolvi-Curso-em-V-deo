#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s1=float(input('Digite o salário do funcionário: R$ '))
a=(s1/100)*15
s2=s1+a
print(f'O salário com o aumento de 15% é: R${s2:.2f}')