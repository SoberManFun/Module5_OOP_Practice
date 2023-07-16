import json

class Model:
	def __init__(self, title, text, author):
		self.title = title
		self.text = text
		self.author = author

	def save(self, filename):
		data = vars(self)  # Получаем все атрибуты объекта в виде словаря
		with open(filename, 'w') as file:
			json.dump(data, file, ensure_ascii=False)

model = Model('Какой-то заголовок', 'Какой-то текст', 'Какой-то автор')

model.save('data.json')

print(list(filter(lambda x: not x.startswith('_'), dir(model))))