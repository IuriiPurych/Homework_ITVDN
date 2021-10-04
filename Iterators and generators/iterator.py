# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).


#MyRange(10) = MyRang(start = 0, end = 10, step = 1)
#MyRange(2, 10) = MyRang(start = 2, end = 10, step = 1)
#MyRange(2, 10, 2) = MyRang(start = 2, end = 10, step = 2)

import math


class MyRange:
	def __init__(self, start, end=None, step=1):
		if end is None:
			self.start = 0
			self.end = start
		else:
			self.start = start
			self.end = end

		if step == 0:
			raise ValueError('Step must not be zero. ')
		else:
			self.step = step

		length = math.ceil((self.end - self.start) / self.step)
		self.length = length if length > 0 else 0

		self.elements_returned = 0
		self.current = None

	def __len__(self):
		return self.length

	def __iter__(self):
		return self

	def __next__(self):
		if self.elements_returned >= self.length:
			raise StopIteration

		self.elements_returned += 1

		if self.current is None:
			self.current = self.start
		else:
			self.current += self.step

		return self.current


def test_len_of_my_range():
	radius = 30
	try:
		for start in range(-radius, radius, 1):
			for end in range(-radius, radius, 1):
				for step in range(-radius, radius, 1):
					if step == 0:
						continue

					my_range = MyRange(start, end, step)
					std_range = range(start, end, step)

					assert len(my_range) == len(std_range)
	except AssertionError:
		print('Start:', start)
		print('end:', end)
		print('step:', step)
		print('len(my_range):', len(my_range))
		print('len(std_range):', len(std_range))
	else:
		print('Test len() complete.')


def test_my_range():
	radius = 30
	try:
		for start in range(-radius, radius, 1):
			for end in range(-radius, radius, 1):
				for step in range(-radius, radius, 1):
					if step == 0:
						continue

					my_range = MyRange(start, end, step)
					std_range = range(start, end, step)

					my_range_list = list(my_range)
					std_range_list = list(std_range)

					assert my_range_list == std_range_list
	except AssertionError:
		print('Start:', start)
		print('end:', end)
		print('step:', step)
		print('len(my_range):', len(my_range))
		print('len(std_range):', len(std_range))
	else:
		print('Test range complete.')


def main():
	for i in MyRange(10, 2, -1):
		print(i)

	print()
	test_my_range()
	test_len_of_my_range()


if __name__ == '__main__':
	main()
