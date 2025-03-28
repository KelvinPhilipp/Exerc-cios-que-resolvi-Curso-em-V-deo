#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
alunos='Klaus', 'Kalel', 'Ethan', 'Karina'
escolhido=random.choice(alunos)
print(f'O aluno sorteado para apagar o quadro foi o {escolhido}')