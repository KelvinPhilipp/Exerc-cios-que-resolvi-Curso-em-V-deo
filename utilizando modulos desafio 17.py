#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

'''forma tradicional de se fazer
cat_oposto=float(input('Digite o comprimento do cateto oposto em cm: '))
cat_adj=float(input('Digite o comprimento do cateto adjacente em cm: '))
hip=(cat_oposto**2+cat_adj**2)**(1/2)
print(f'Sendo o valor do cateto oposto {cat_oposto} e o valor do cateto adjacente {cat_adj} temos a hipotenusa com valor de: {hip:.2f} cm')'''


#FORMA IMPORTANTO BIBLIOTECA MATH
import math
cat_oposto=float(input('Digite o comprimento do cateto oposto em cm: '))
cat_adj=float(input('Digite o comprimento do cateto adjacente em cm: '))
hip=math.hypot(cat_oposto, cat_adj)
print(f'Sendo o valor do cateto oposto {cat_oposto} cm e o valor do cateto adjacente {cat_adj} cm, temos a hipotenusa com valor de: {hip:.2f} cm')