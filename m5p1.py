#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ1_НАЧАЛО____________________
# class StringVar:
# 	def __init__(self):
# 		self.string = ''

# 	def set(self, new_string):
# 		self.string = new_string

# 	def get(self):
# 		return self.string

# string1 = StringVar()
# print('Базовое значение:', string1.get())

# string1.set('''В ООП выделяют четыре основных элемента: классы, объекты, методы и атрибуты.
# Объектно-ориентированный подход к программированию строится на трёх основных принципах: наследование, инкапсуляция и полиморфизм.
# Программы, созданные по принципам ООП, более структурированные, легче читаются и хорошо масштабируются.''')

# print('Новое значение:', string1.get())
#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ1_КОНЕЦ____________________

#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ2_НАЧАЛО____________________
# class Point:
# 	def __init__(self, x=0, y=0):
# 		self.x = x
# 		self.y = y

# 	def set_x(self, x):
# 		self.x = x

# 	def set_y(self, y):
# 		self.y = y

# 	def get_x(self):
# 		return self.x

# 	def get_y(self):
# 		return self.y

# 	def distance(self, other_point):
# 		dx = self.x - other_point.x
# 		dy = self.y - other_point.y
# 		return (dx ** 2 + dy ** 2) ** 0.5

# point1 = Point(3, 4)
# print('Координаты точки 1:', point1.get_x(), point1.get_y())

# point1.set_x(5)
# point1.set_y(2)
# print('Новые координаты точки 1:', point1.get_x(), point1.get_y())

# point2 = Point(1, 2)
# print('Координаты точки 2:', point2.get_x(), point2.get_y())

# distance1 = point1.distance(point2)
# print('Расстояние между точками 1 и 2:', distance1)

#___________________МОДУЛЬ_5_ЧАСТЬ_1_УРОВЕНЬ2_КОНЕЦ____________________