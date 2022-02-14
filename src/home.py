from bottle import route, jinja2_view as view, error, static_file
import src.fla as fla
import os
import logging

PREFIX_ROUTE = ''

@route(PREFIX_ROUTE + '/hello')
def hello():
    return "Hello World!"


@route(PREFIX_ROUTE + '/')
@view('src/index.html')
def index():
    return dict()


@route(PREFIX_ROUTE + '/calendar')
@view('src/calendar.html')
def calendar():
    # calendar = fla.get_calendar(3344)
    calendar = fla.get_calendar(4077)
    return dict(journees=sorted(calendar, key=lambda journee:journee['Date'], reverse=True))


@route(PREFIX_ROUTE + '/classement11/<year>')
@view('src/classement.html')
def classement11(year=None):

    dict_classements = dict()
    dict_classements['2022'] = dict(championnat_id=1277, saison_id=10)
    dict_classements['2021'] = dict(championnat_id=1252, saison_id=9)

    infos = dict_classements[year]
    return fla.get_classement(infos['championnat_id'], saison_id=infos['saison_id'])


@error(500)
def error500(error):
    logging.info(error)
    print(error)    
    return 'Oups, une erreur est survenue'

@route(PREFIX_ROUTE + '/static/<filename>')
def server_static(filename):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return static_file(filename, root=dir_path + '/static')


@route(PREFIX_ROUTE + '/opponents')
@view('src/opponents.html')
def opponents():
    return fla.fetch_opponents()
