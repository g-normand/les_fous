
APP_PATH := $(CURDIR)/src
ENV_PATH := $(CURDIR)

# For shell to bash to be able to use source.
SHELL = /bin/bash
# Shortcut to set env command before each python cmd.
VENV = source $(ENV_PATH)/bin/activate

# Config is based on two environment files, initalized here.
virtualenv: $(ENV_PATH)/bin/activate

$(ENV_PATH)/bin/activate:
	virtualenv -p /usr/bin/python3.9 $(ENV_PATH)

install: virtualenv
	$(VENV) && pip3 install -r requirements.txt

install_alwaysdata: virtualenv
	 python -m pip install -r requirements.txt

start: virtualenv
	$(VENV) && python start-bottle.py
