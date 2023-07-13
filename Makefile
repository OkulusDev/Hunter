PYTHON=python3
PIP=pip3
TYPE_OF_HUNTER=cli
PIP_REQIREMENTS=requirements.txt

run:
	$(PYTHON) hunter.py

depends:
	$(PIP) install -r $(PIP_REQUIREMENTS)
