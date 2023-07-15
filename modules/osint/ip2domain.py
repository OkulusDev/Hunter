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
import socket
import requests

def get_ip(hostname):
	try:
		ip = socket.gethostbyname(hostname)
		return ip
	except Exception as e:
		return f"[!] Произошла ошибка: {e}"

def get_server_name(hostname, fua):
	try:
		headers = {
			'User-Agent': fua
		}
		content = requests.get(hostname, headers=headers)
		server = content.headers['Server']

		return server
	except Exception as e:
		return "[!] Произошла ошибка: {e}"
		