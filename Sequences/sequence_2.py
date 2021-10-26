# Создайте функцию от произвольного количества аргументов, которая вычисляет среднее арифметическое данных чисел.
# Вычислите при помощи неё среднее арифметическое двух заданных чисел и среднее арифметическое чисел
# из заданного диапазона.

def some(*args: [int]) -> float:
	_sum: int = 0
	count: int = 0
	if len(args) <= 1:
		raise TypeError('The Some-function need two or more arguments.')

	if len(args) == 2 and args[0] < args[1]:
		for item in range(args[0], args[1]):
			_sum += item
		count = len(range(args[0], args[1]))
	for item in args:
		_sum += item
		count += 1

	return _sum / count


print(some(2, 4))
print(some(2, 4, 6))
print(some(2111, 411212))
