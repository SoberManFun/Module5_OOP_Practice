#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ3_БЛОК_3_1____________________
import random

class Warrior:
	def __init__(self, name):
		self.health = 100
		self.name = name

	def attack(self, enemy):
		enemy.health -= 20

		if enemy.health < 0:
			enemy.health = 0

		print('Юнит атакован! Здоровье воина:', enemy.name, ' = ', enemy.health)

warrior1 = Warrior('Воин1')
warrior2 = Warrior('Воин2')

while warrior1.health > 0 and warrior2.health > 0:
	attacker = random.choice([warrior1, warrior2])
	defender = warrior2 if attacker == warrior1 else warrior1

	attacker.attack(defender)

if warrior1.health == 0:
	print('Победил второй юнит!')
else:
	print('Победил первый юнит!')
#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ3_БЛОК_3_1____________________