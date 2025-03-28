#O mesmo professor do desafio anterior quer sortear a ordem de apresentção de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
alunos='Klaus Kalel Ethan Karina'.split()
random.shuffle(alunos)
print(f'A ordem de apresentação será a seguinte: {alunos}')