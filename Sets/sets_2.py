# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок.
# Должна быть реализована возможность ввода изначальной ссылки и короткого названия
# и получения изначальной ссылки по её названию.
import random
import string
from typing import Optional, Dict

import validators


class SETTINGS:
	LENGTH_LINK: int = 4
	DOMAIN: str = 'https://lk.tr/'


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
	print('Select a menu item:\n'
		  '	1. Input full link.\n'
		  '	2. Input short link. \n'
		  '	3. Show all links.\n'
		  '	4. Exit.')


def show_all_links(links: Dict[str, str], domain: str):
	for key in links:
		print(f'Long link: {links[key]}\n Short link: {domain + key}')


def get_short_link(links: Dict[str, str], domain: str):
	url: str = input('Input short link:')
	if validators.url(url):
		key: str = url.removeprefix(domain)
		print(f'The long link is {links[key]}') if key in links else print(f'The short link {url} not found.')
	else:
		print('The link is wrong.')


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
			get_short_link(links, SETTINGS.DOMAIN)
		elif item_menu == '3':
			show_all_links(links, SETTINGS.DOMAIN)
		elif item_menu == '4':
			break
		else:
			print('Incorrect menu item.')


if __name__ == '__main__':
	main()
