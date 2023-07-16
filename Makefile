PYTHON=python3
PIP=pip3
TYPE_OF_HUNTER=cli
PIP_REQUIREMENTS=requirements.txt
PKG_MNGR=apt

run:
	$(PYTHON) hunter.py

make rootrun:
	sudo $(PYTHON) hunter.py

install:
	sudo $(PKG_MNGR) install whois python3 python3-pip 
	$(PIP) install -r $(PIP_REQUIREMENTS)

rootinstall:
	sudo $(PKG_MNGR) install whois python3 python3-pip 
	sudo $(PIP) install -r $(PIP_REQUIREMENTS)

depends:
	echo "[EN] Please, use command 'make install'"
	echo "[RU] Пожалуйста, используйте команду 'make install'"
