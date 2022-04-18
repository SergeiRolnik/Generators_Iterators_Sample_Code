nested_list = [['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None]]

# Задание №1
class FlatIterator:

	def __init__(self, list):
		self.list = list
		self.main_cursor = -1
		self.list_lenght = len(self.list)

	def __iter__(self):
		self.main_cursor += 1
		self.nested_cursor = 0
		return self

	def __next__(self):
		if self.nested_cursor == len(self.list[self.main_cursor]):
			iter(self)
		if self.main_cursor == self.list_lenght:
			raise StopIteration
		self.nested_cursor += 1
		return self.list[self.main_cursor][self.nested_cursor - 1]

print('------- Задание №1 ----------------')
for item in FlatIterator(nested_list):
	print(item)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)

# Задание №2
def flat_generator(list):
	for el1 in list:
		for el2 in el1:
			yield el2

print('------- Задание №2 ----------------')
for item in flat_generator(nested_list):
	print(item)

# Задание №4
nested_list = [1, 2, ['a', 'b', [1, 2, 3, ['a', 'b', 'c']]],['d', 'e', 'f', 'h', False],[1, ['a', 'b', 'c'], None],[1, 2]]

def flat_generator_nested(my_list):
	for el in my_list:
		if type(el) == list:
			yield from flat_generator_nested(el)
		else:
			yield el

print('------- Задание №4 ----------------')
for item in flat_generator_nested(nested_list):
	print(item)