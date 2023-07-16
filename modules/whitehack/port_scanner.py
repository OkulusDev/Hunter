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
from datetime import datetime
import sys


def scan_ports(hostname):
	start = datetime.now()

	ports = {
		20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
		25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
		115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP",
		179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
		514: "SYSLOG", 515: "PRINTER", 993: "IMAPS",
		995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
		1433: "SQL Server", 1723: "PPTP", 3128: "HTTP",
		3268: "LDAP", 3306: "MySQL", 3389: "RDP",
		5432: "PostgreSQL", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin"
	}

	open_ports = []
	closed_ports = []
	full_ports = [i for i in range(1, 65355)]

	ip = socket.gethostbyname(hostname)

	for port in range(65535):
		cont = socket.socket()
		cont.settimeout(1)

		try:
			cont.connect((ip, port))
		except socket.error:
			print(f'[!] Порт {port} закрыт')
			closed_ports.append([port])
		else:
			try:
				print(f"[{socket.gethostbyname(ip)}:{str(port)}] открыт/{ports[port]}")
				open_ports.append({port, ports[port]})
			except KeyError:
				print(f"[{socket.gethostbyname(ip)}:{str(port)}] открыт/неизвестный тип")
				open_ports.append({port, 'неизвестный тип'})
			finally:
				cont.close()

	ends = datetime.now()
	print("<Время работы:{}>".format(ends - start))

	print('[+] Закрытые порты: ')
	for closed_port in closed_ports:
		print(closed_port, end=', ')

	print()

	print('[+] Открытые порты: ')
	for open_port in open_ports:
		print(open_port)
