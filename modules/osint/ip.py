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
import os
import requests


def get_info_about_ip(ipaddr, fua):
	try:
		headers = {
			'User-Agent': fua
		}
		info_data = requests.get(f'https://ipinfo.io/{ipaddr}/json', headers=headers).json()
	except Exception as ex:
		print("\n[!] Произошла ошибка")
		print(f'''Ошибка: {ex}''')
		return

	whois_info = os.popen(f'whois {ipaddr}').read().strip()

	print("⣿" * 10)

	print(f'IP: {info_data.get("ip")}')
	print(f'Город: {info_data.get("city")}')
	print(f'Регион: {info_data.get("region")}')
	print(f'Страна: {info_data.get("country")}')
	print(f'Имя хоста: {info_data.get("hostname")}')
	print(f'JSON данные: {info_data}')

	print("⣿" * 30)
	print(whois_info)
	print("⣿" * 30)
	print()
