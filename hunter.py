#!/usr/bin/python3
# -*- coding:utf-8 -*-
#!/usr/bin/python3
"""Hunter - is a pack of programs for interacting with the Internet, for conducting penetration testing, working with Linux and OSINT
Copyright (C) 2022, 2023 Okulus Dev (Alexeev Bronislav)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more detailsession.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
import sys																# Импорт библиотеки sys
from random import randint												# Импорт библиотеки рандома

# Библиотеки
from libs.style import cls, FG, BG, Style								# Импорт локальной библиотеки цветов
from libs.style import logo, menu

# Модули анонимности
import modules.anonymity.fakeuseragent as fakeuseragent 				# Импорт модуля фейкового user agent
import modules.anonymity.machanger as machanger							# Импорт модуля замены MAC

# Модули белого хакинга
import modules.whitehack.sqlinj_scanner as sqlinj_scanner				# Импорт модуля сканирования SQL-инъекций
import modules.whitehack.xss_scanner as xss_scanner 					# Импорт модуля сканирования XSS уязвимостей

# Модули OSINT технологий
import modules.osint.ip as osintip										# Импорт модуля поиска информации по IP
import modules.osint.phone as osintphone								# Импорт модуля поиска информации по номеру телефона
import modules.osint.ip2domain as iphost_osint  						# Импорт модуля получения IP/сервера
import modules.osint.linksextract as extractlinks						# Импорт модуля получения ссылок с сайта


def clear_bg():
	cls()
	Style.write(BG.rgb(11, 11, 11) + FG.rgb(64, 224, 208))


def interactive_mode():
	"""Интерактивный режим"""

	while True:
		# Бесконечный цикл
		clear_bg()

		for line in menu.split('\n'):
			# Выводим меню
			Style.write(f'{line}\n')

		# Запращиваем вывод у пользователя
		cmd = input(' > ')

		# Обработка команд
		if cmd == '0':
			cls()
			sys.exit()
		elif cmd == '1':
			# Замена MAC-Адреса
			clear_bg()
			print(machanger.ifconfig())
			machanger.main(input('Введите название интерфейса >>> '))
		elif cmd == '2':
			# Генерация фейкового User-Agent
			fua = fakeuseragent.generate_useragent()
			Style.write(f'User-Agent: {fua}\n')
		elif cmd == "3":
			# Сканнер SQL-инъекций
			fua = fakeuseragent.generate_useragent()
			sqlinj_scanner.scanning(fua, input('Введите ссылку на сайт >>> '))
		elif cmd == '4':
			fua = fakeuseragent.generate_useragent()
			xss_scanner.scan_xss(input('Введите ссылку на сайт >>> '), fua)
		elif cmd == '5':
			fua = fakeuseragent.generate_useragent()
			osintip.get_info_about_ip(input('Введите IP-адрес >>> '), fua)
		elif cmd == '6':
			fua = fakeuseragent.generate_useragent()
			osintphone.get_info_phonenumber(input('Введите номер телефона >>> '), fua)
		elif cmd == '7':
			iphost_osint.get_ip(input('Введите ссылку на сайт (без протокола) >>> '))
		elif cmd == '8':
			fua = fakeuseragent.generate_useragent()
			iphost_osint.get_server_name(input('Введите ссылку на сайт'), fua)
		elif cmd == '9':
			extractlinks.internal_urls = set()
			extractlinks.external_urls = set()
			target_url = input('Введите ссылку на страницу >>> ')

			try:
				extractlinks.get_links(target_url, int(input('Введите максимальное количество ссылок для проверки >>> ')))
			except ValueError:
				print('[!] Вы ввели не число. Используется значение по умолчанию (30)')
				extractlinks.get_links(target_url, 30)
		else:
			Style.write(FG.red + f"Команда {cmd} не найдена\n")

		input('Нажмите Enter чтобы продолжить . . . ')

	clear_bg()
	exit()


if __name__ == '__main__':
	"""Если файл исполняемый, а не импортируется"""

	# Заполняем рабочее пронстранство
	Style.write(BG.rgb(11, 11, 11) + FG.rgb(64, 224, 208))
	Style.write(Style.clear)
	Style.write(Style.top)

	for line in logo.split('\n'):
		# Выводим лого
		Style.writew(f"{line}\n", 0.002)

	# Входим в интерактивный режим
	interactive_mode()
