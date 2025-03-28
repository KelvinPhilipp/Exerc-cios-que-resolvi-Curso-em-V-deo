#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ângulo=float(input('Digite o ângulo: '))
cos=math.cos(math.radians(ângulo))
sen=math.sin(math.radians(ângulo))
tan=math.tan(math.radians(ângulo))
print(f'O cosseno de {ângulo} é: {cos:.2f} \n o seno de {ângulo} é: {sen:.2f} \n e a tangente de {ângulo} é: {tan:.2f}')
#necessitei usat math.radians pq a funcionalidade cos, sen e tan calculam esses valores das radianas e não diretamente do ângulo, por isso é necessário primeiro calcular os radianos para depois calcular o cos, sen e tan do radiano.
