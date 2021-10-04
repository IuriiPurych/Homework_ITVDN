# Напишите функцию-генератор для получения n первых простых чисел.

def simple_numbers_generator(count):
	for number in range(1, count):
		for i in range(2, number + 1):
			if number % i == 0:
				if number == i:
					yield number
				else:
					break


for num in simple_numbers_generator(100):
	print(num)
