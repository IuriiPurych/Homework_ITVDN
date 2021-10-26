# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок.
# Должна быть реализована возможность ввода изначальной ссылки и короткого названия
# и получения изначальной ссылки по её названию.
import random
import string
from typing import Optional, Dict

import validators


class MyLink:
	class SETTINGS:
		LENGTH_LINK: int = 4
		DOMAIN: str = 'https://lk.tr/'

	def __init__(self):
		# todo: надо продумать передалть на класс
		pass

	def add(self, key, value):
		# todo: переписать на класс
		pass


def get_long_link() -> Optional[str]:
	url: str = input('Input long link:')
	if validators.url(url):
		return url
	else:
		print('The link is wrong.')
		return None


def get_random_string(length: int) -> str:
	link = ''.join(random.choice(string.ascii_letters) for _ in range(length))
	return link


def print_menu():
	print('''Select a menu item:
			1. Input full link.
			2. Input long link. 
			3. Show all links.
			4. Exit.''')


def show_all_links():
	pass


def main():
	links: Dict[str, str] = {}
	while True:
		print_menu()
		item_menu: str = input()
		if item_menu == '1':
			long_link = get_long_link()
			if long_link is not None:
				key = get_random_string(SETTINGS.LENGTH_LINK)
				while key in links:
					key = get_random_string(SETTINGS.LENGTH_LINK)
				links[key] = long_link
				print(links)
		elif item_menu == '2':
			get_short_link()
		elif item_menu == '3':
			show_all_links()
		elif item_menu == '4':
			break
		else:
			print('Incorrect menu item.')


if __name__ == '__main__':
	main()
