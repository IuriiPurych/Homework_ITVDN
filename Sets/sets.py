#Даны две строки. Выведите на экран символы, которые есть в обоих строках.

str1 = 'asdfghjkl'
str2 = 'azsxdcfvgbhnjmk,'

for ch in str1:
	if ch in str2:
		print(ch)
