dias=int(input('Quantos dias alugados? '))
km=float(input('Quantos km rodados? '))
valor_dia=dias*60
valor_km=km*0.15
total=valor_km+valor_dia
print(f'O valor total a ser pago é de: R${total:.2f}')