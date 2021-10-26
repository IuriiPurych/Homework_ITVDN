# Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова данного текста.

words = input('Input a text:').split()

print(type(words))
print(sorted(words))