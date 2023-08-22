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
import argparse 														# Импорт библиотеки для аргументов командной строки

# Библиотеки
from libs.style import cls, FG, BG, Style								# Импорт локальной библиотеки цветов
from libs.style import logo, menu

# Модули анонимности
import modules.anonymity.fakeuseragent as fakeuseragent 				# Импорт модуля фейкового user agent
import modules.anonymity.machanger as machanger							# Импорт модуля замены MAC

# Модули белого хакинга
import modules.scanners.sqlinj_scanner as sqlinj_scanner				# Импорт модуля сканирования SQL-инъекций
import modules.scanners.xss_scanner as xss_scanner 					# Импорт модуля сканирования XSS уязвимостей
import modules.scanners.port_scanner as port_scanner
import modules.scanners.synport_scanner as synport_scanner

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
			machanger.main(input('Enter interface name >>> '))
		elif cmd == '2':
			# Генерация фейкового User-Agent
			fua = fakeuseragent.generate_useragent()
			Style.write(f'User-Agent: {fua}\n')
		elif cmd == "3":
			# Сканнер SQL-инъекций
			fua = fakeuseragent.generate_useragent()
			sqlinj_scanner.scanning(fua, input('Enter link >>> '))
		elif cmd == '4':
			# Сканнер xss-инъекций
			fua = fakeuseragent.generate_useragent()
			xss_scanner.scan_xss(input('Enter link >>> '), fua)
		elif cmd == '5':
			# Сканнер портов
			port_scanner.scan_ports(input('Enter link or IP address >>> '))
		elif cmd == '6':
			# SYN сканнер портов
			synport_scanner.start_scan(input('Enter link or IP address >>> '))
		elif cmd == '7':
			# Информация об IP адресе
			fua = fakeuseragent.generate_useragent()
			osintip.get_info_about_ip(input('Enter IP address >>> '), fua)
		elif cmd == '8':
			# Информация о номере телефона
			fua = fakeuseragent.generate_useragent()
			osintphone.get_info_phonenumber(input('Enter phone number >>> '), fua)
		elif cmd == '9':
			print(iphost_osint.get_ip(input('Enter link >>> ')))
		elif cmd == '10':
			fua = fakeuseragent.generate_useragent()
			iphost_osint.get_server_name(input('Enter link'), fua)
		elif cmd == '11':
			extractlinks.internal_urls = set()
			extractlinks.external_urls = set()
			target_url = input('Enter link >>> ')

			try:
				extractlinks.get_links(target_url, int(input('Enter max links count >>> ')))
			except ValueError:
				print('[!] You dont enter number. Used default number (30)')
				extractlinks.get_links(target_url, 30)
		else:
			Style.write(FG.red + f"Command {cmd} not found\n")

		input('Press enter to continue . . . ')

	clear_bg()
	exit()


if __name__ == '__main__':
	"""Если файл исполняемый, а не импортируется"""

	if len(sys.argv) > 1:
		# Режим аргументов командной строки
		parser = argparse.ArgumentParser(description='Hunter - is a pack of programs for interacting with the Internet, for conducting penetration testing, working with Linux and OSINT')
		parser.add_argument('--random-mac', type=str,
							help='Generate a random mac address')
		parser.add_argument('--sqlinj-scanner', type=str,
							help='Scanning the site for sql injections')
		parser.add_argument('--xss-scanner', type=str,
							help='Scanning the site for xss vulnerabilities')
		parser.add_argument('--scan-ports', type=str,
							help='Port Scanning')
		parser.add_argument('--syn-scan-ports', type=str,
							help='SYN Port Scanning')
		parser.add_argument('--ip-info', type=str,
							help='Get information about IP address')
		parser.add_argument("--phone-info", type=str,
							help='Get information about phone number')
		parser.add_argument("--ip2host", type=str,
							help='Get hostname by IP address')

		args = parser.parse_args()
		fua = fakeuseragent.generate_useragent()

		# Проверяем аргументы
		if args.random_mac:
			machanger.main(args.random_mac)
		elif args.sqlinj_scanner:
			sqlinj_scanner.scanning(fua, args.sqlinj_scanner)
		elif args.xss_scanner:
			xss_scanner.scan_xss(args.xss_scanner, fua)
		elif args.scan_ports:
			port_scanner.scan_ports(args.scan_ports)
		elif args.syn_scan_ports:
			synport_scanner.start_scan(args.syn_scan_ports)
		elif args.ip_info:
			osintip.get_info_about_ip(args.ip_info, fua)
		elif args.phone_info:
			osintphone.get_info_phonenumber(args.phone_info, fua)
		elif args.ip2host:
			print(iphost_osint.get_ip(args.ip2host))
	else:
		# Заполняем рабочее пронстранство
		Style.write(BG.rgb(11, 11, 11) + FG.rgb(64, 224, 208))
		Style.write(Style.clear)
		Style.write(Style.top)

		for line in logo.split('\n'):
			# Выводим лого
			Style.writew(f"{line}\n", 0.0015)

		# Входим в интерактивный режим
		interactive_mode()
