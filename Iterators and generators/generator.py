#Напишите генератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).

def my_generator(start, end=None, step=1) -> int:
	if end is None:
		start, end = 0, start
	current = end
	if step <= 0:
		raise ValueError('Step must be positive.')

	while current >= start:
		yield current
		current -= step


my_gen = my_generator(-10, 5, 2)
for i in my_gen:
	print(i)
