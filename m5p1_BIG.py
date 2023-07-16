#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ3_БЛОК_3_1____________________
# import random

# class Warrior:
# 	def __init__(self, name):
# 		self.health = 100
# 		self.name = name

# 	def attack(self, enemy):
# 		enemy.health -= 20

# 		if enemy.health < 0:
# 			enemy.health = 0

# 		print('Юнит атакован! Здоровье воина:', enemy.name, ' = ', enemy.health)

# warrior1 = Warrior('Воин1')
# warrior2 = Warrior('Воин2')

# while warrior1.health > 0 and warrior2.health > 0:
# 	attacker = random.choice([warrior1, warrior2])
# 	defender = warrior2 if attacker == warrior1 else warrior1

# 	attacker.attack(defender)

# if warrior1.health == 0:
# 	print('Победил второй юнит!')
# else:
# 	print('Победил первый юнит!')
#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ3_БЛОК_3_1____________________

#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ3_БЛОК_3_2____________________
# import random

# class Warrior:
# 	def __init__(self, name):
# 		self.health = 100
# 		self.armor = 100
# 		self.endurance = 100
# 		self.name = name

# 	def attack(self, enemy):
# 		self.endurance -= 10

# 		if self.endurance <= 0:
# 			damage = random.randint(0, 10)
# 		else:
# 			damage = random.randint(10, 30)

# 		enemy.defend(damage)
# 		print('Юнит атакован! Здоровье:', self.name, ' = ', self.health)

# 	def defend(self, damage):
# 		if self.armor > 0:
# 			self.armor_loss = random.randint(0, 10)
# 			self.armor -= self.armor_loss
# 			self.health_loss = random.randint(0, 20)
# 			self.health -= self.health_loss
# 		else:
# 			self.armor_loss = 0
# 			self.health_loss = random.randint(10, 30)
# 			self.health -= self.health_loss
# 		print('Юнит защищается! Здоровье:', self.name, ' = ', self.health)

# warrior1 = Warrior('Sub Zero')
# warrior2 = Warrior('Noob Saibot')

# while warrior1.health > 10 and warrior2.health > 10:

# 	action_warrior1 = random.choice(['attack', 'defend'])
# 	action_warrior2 = random.choice(['attack', 'defend'])

# 	if action_warrior1 == 'attack' and action_warrior2 == 'attack':
# 		warrior1.attack(warrior2)
# 		warrior2.attack(warrior1)
# 	elif action_warrior1 == 'attack' and action_warrior2 == 'defend':
# 		warrior1.attack(warrior2)
# 		warrior2.defend(0)
# 	elif action_warrior1 == 'defend' and action_warrior2 == 'attack':
# 		warrior1.defend(0)
# 		warrior2.attack(warrior1)
# 	elif action_warrior1 == 'defend' and action_warrior2 == 'defend':
# 		warrior1.defend(0)
# 		warrior2.defend(0)

# if warrior1.health <= 10:
# 	choice = input(warrior1.name + ' проиграл. Убить его? (да/нет): ')
# 	if choice.lower() == 'да':
# 		warrior1.health = 0
# 	else:
# 		print(warrior1.name + ' проиграл, но Помилован!')	

# if warrior2.health <= 10:
# 	choice = input(warrior2.name + ' проиграл. Убить его? (да/нет): ')
# 	if choice.lower() == 'да':
# 		warrior2.health = 0
# 	else:
# 		print(warrior2.name + 'проиграл, но Помилован!')	

# if warrior1.health == 0 and warrior2.health == 0:
# 	print('Оба воина проиграли!')
# elif warrior1.health == 0:
# 	print(warrior1.name, ' проиграл и убит! -=FATALITY=-')
# elif warrior2.health == 0:
# 	print(warrior2.name, ' проиграл и убит! -=FATALITY=-')
#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ3_БЛОК_3_2____________________