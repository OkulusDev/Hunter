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
from random import randint
from time import sleep

from libs.style import cls, FG, BG, Style								# Импорт локальной библиотеки цветов

def interactive_mode():
	while True:
		cls()
		Style.write(BG.rgb(11, 11, 11) + FG.rgb(64, 224, 208))
		cmd = input(' > ')


if __name__ == '__main__':
	Style.write(BG.rgb(210, 210, 210) + FG.rgb(50, 50, 50) + Style.bold + "Welcome!\n")
	Style.write(BG.rgb(11, 11, 11) + FG.rgb(64, 224, 208))
	Style.write(Style.clear)
	Style.write(Style.top)
	Style.writew("Загрузка библиотек", 0.05)
	Style.writew("." * randint(2, 6))
	Style.write()
	Style.writew("Загрузка модулей", 0.05)
	Style.writew("." * randint(2, 6))
	Style.write()
	Style.writew("Финальная очистка", 0.05)
	Style.writew("." * randint(2, 6))

	interactive_mode()
