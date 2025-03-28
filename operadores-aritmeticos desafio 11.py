p1=float(input('Qual é a altura da parede em metros? Não arredonde a medida: '))
p2=float(input('Qual é a altura da parede em metros? Não arredonde a medida: '))
a=p1*p2
print(f'A área da parede é {a}m²')
#Tinta a cada 1 litro pinta 2m^2
t=2
n=a/t
print(f'Você precisará de {n} litros de tinta para total cobertura da parede')
#Mostrar quantos litros de tinta são necessários para pintar uma parede, considerando que 1 litro de tinta pinta 2m^2