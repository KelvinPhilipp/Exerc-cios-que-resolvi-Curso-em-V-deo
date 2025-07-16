#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual é o valor do salário do funcionário? '))

if salario > 1250:
    salario = salario + ((salario/100)*10)

else:
    salario = salario + ((salario/100)*15)

print(f'O novo valor do salário com aumento é {salario}')
