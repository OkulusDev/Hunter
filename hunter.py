#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""Hunter - Tool for OSINT, networking and ethical hacking
Copyright (C) 2023  Okulus Dev

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>"""
import sys																# Импорт библиотеки sys
from random import randint												# Импорт библиотеки рандома

# Библиотеки
from libs.style import cls, FG, BG, Style								# Импорт локальной библиотеки цветов

# Модули
import modules.fakeuseragent as fakeuseragent 							# Импорт модуля фейкового user agent
import modules.machanger as machanger									# Импорт модуля замены MAC
import modules.sqlinj_scanner as sqlinj_scanner							# Импорт модуля сканирования SQL-инъекций
import modules.xss_scanner as xss_scanner 								# Импорт модуля сканирования XSS уязвимостей

menu = """
   ██░ ██   █    ██   ███▄    █  ▄▄▄█████▓ ▓█████   ██▀███  
  ▓██░ ██▒  ██  ▓██▒  ██ ▀█   █  ▓  ██▒ ▓▒ ▓█   ▀  ▓██ ▒ ██▒
  ▒██▀▀██░ ▓██  ▒██░ ▓██  ▀█ ██▒ ▒ ▓██░ ▒░ ▒███    ▓██ ░▄█ ▒
  ░▓█ ░██  ▓▓█  ░██░ ▓██▒  ▐▌██▒ ░ ▓██▓ ░  ▒▓█  ▄  ▒██▀▀█▄  
  ░▓█▒░██▓ ▒▒█████▓  ▒██░   ▓██░  ▒██▒ ░ ░ ▒████▒░  ██▓ ▒██▒
   ▒ ░░▒░▒ ░▒▓▒ ▒ ▒  ░ ▒░   ▒ ▒   ▒ ░░   ░ ░ ▒░ ░░  ▒▓ ░▒▓░
   ▒ ░▒░ ░ ░░▒░ ░ ░  ░ ░░   ░ ▒░    ░      ░ ░  ░   ░▒ ░ ▒░
   ░  ░░ ░  ░░░ ░ ░    ░   ░ ░   ░         ░      ░░   ░ 
   ░  ░  ░    ░              ░             ░  ░    ░     

      ╔════════════════════════════════════════════════╗
      ║                     Другое                     ║
      ║ 0 - Выход                                      ║
      ║                   Анонимность                  ║
      ║ 1. Замена MAC-адреса                           ║
      ║ 2. Генерация фейкового User-Agent              ║
      ║                     Сканнеры                   ║
      ║ 3. Сканнер SQL-инъекций                        ║
      ║ 4. Сканнер XSS-уяизвимостей                    ║
      ╚════════════════════════════════════════════════╝
"""


def clear_bg():
	cls()
	Style.write(BG.rgb(11, 11, 11) + FG.rgb(64, 224, 208))


def interactive_mode():
	while True:
		clear_bg()

		for line in menu.split('\n'):
			Style.write(f'{line}\n')

		cmd = input(' > ')

		if cmd == '0':
			cls()
			sys.exit()
		elif cmd == '1':
			clear_bg()
			print(machanger.ifconfig())
			machanger.main(input('Введите название интерфейса >>> '))
		elif cmd == '2':
			fua = fakeuseragent.generate_useragent()
			Style.write(f'User-Agent: {fua}\n')
		elif cmd == "3":
			fua = fakeuseragent.generate_useragent()
			sqlinj_scanner.scanning(fua, input('Введите ссылку на сайт >>> '))
		elif cmd == '4':
			...

		input('Нажмите Enter чтобы продолжить . . . ')


if __name__ == '__main__':
	Style.write(BG.rgb(210, 210, 210) + FG.rgb(50, 50, 50) + Style.bold + "Welcome!\n")
	Style.write(BG.rgb(11, 11, 11) + FG.rgb(64, 224, 208))
	Style.write(Style.clear)
	Style.write(Style.top)
	Style.writew("Загрузка Hunter...", 0.02)
	Style.writew("." * randint(1, 5))

	interactive_mode()
