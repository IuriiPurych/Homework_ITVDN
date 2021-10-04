# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).
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
			self.current = self.end
		else:
			self.current -= self.step

		return self.current


def main():
	for i in MyRange(2, 10, 1):
		print(i)


if __name__ == '__main__':
	main()
