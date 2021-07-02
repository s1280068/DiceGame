name = input('What is your name?\n> ')
print(f'Hello, {name}!')

import random

print('Rolling the dice...')

Dice = []
Dice.append(random.randint(1,6))
Dice.append(random.randint(1,6))

print(f'Die 1: {Dice[0]}')
print(f'Die 1: {Dice[1]}')
print(f'Total value: {sum(Dice)}')
