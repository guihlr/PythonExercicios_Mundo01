# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100),
           randint(1, 100), randint(1, 100))
print('Os valores sorteador foram: ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO maior valor foi {max(numeros)}'
      f'\nO menor valor foi {min(numeros)}')
