# Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её отсортированной
# в порядке возрастания.


my_list = []
while True:
	a = input('Please input an integer. For exit, input exit:')
	if a != 'exit':
		try:
			my_list.append(int(a))
		except ValueError:
			print('Please enter an integer.')
		continue
	break
print(my_list)
print(sorted(my_list))

