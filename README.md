# les_fous

Récupération des données des Fous sur le site de la FLA


Utilisation de Bottle (https://bottlepy.org/docs/dev/)

Tout passe par le WSGI
Pour Alwaysdata, c'est dans /admin/config/uwsgi
"""
chdir = /home/lesfous/www
wsgi-file = /home/lesfous/www/wsgi.py
"""

Sinon faire:
source bin/activate
python start-bottle.py


Pour l'installation:
$ cd /tmp
$ wget --no-check-certificate https://pypi.python.org/packages/source/v/virtualenv/virtualenv-15.0.0.tar.gz
$ tar -vxf virtualenv-15.0.0.tar.gz
$ cd virtualenv-15.0.0/
$ python virtualenv.py  -p python3 --no-site-package $PROJECT_ROOT
$ cd $PROJECT_ROOT
$ source bin/activate
$ pip install bottle requests jinja2
