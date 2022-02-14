# les_fous

Récupération des données des Fous sur le site de la FLA


Utilisation de Bottle (https://bottlepy.org/docs/dev/)

Tout passe par le WSGI
Pour Alwaysdata, c'est dans /admin/config/uwsgi
```
chdir = /home/lesfous/www
wsgi-file = /home/lesfous/www/wsgi.py

L installation est:
make install_alwaysdata
``` 

Sinon faire:
```
make start
```


Pour l'installation:
```
$ git clone git@github.com:g-normand/les_fous.git
$ cd les_fous
$ make install
``` 
