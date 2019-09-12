from bottle import route, jinja2_view as view, error, static_file
import src.fla as fla
import logging

@route('/hello')
def hello():
    return "Hello World!"

@route('/')
@view('src/index.html')
def index():
    return dict()

@error(500)
def error500(error):
    logging.info(error)
    print(error)    
    return 'Oups, une erreur est survenue'

@route('/calendar')
@view('src/calendar.html')
def calendar():
    calendar = fla.get_calendar(2958)
    calendar_7 = fla.get_calendar(3041)
    calendar.extend(calendar_7)
    return dict(journees=sorted(calendar, key=lambda journee:journee['Date'], reverse=True))

@route('/classement11/<year>')
@view('src/classement.html')
def classement11(year=None):
    print(year)
    if year == '2019':
        return fla.get_classement(1170, saison_id=6)
    if year == '2018':
        return fla.get_classement(1144, saison_id=5)
    if year == '2017':
        return fla.get_classement(1122, saison_id=3)
    if year == '2016':
        return fla.get_classement(6, saison_id=2)
    return fla.get_classement(1205, saison_id=7)

@route('/classement7/<year>')
@view('src/classement.html')
def classement7(year=None):
    if year == '2019':
        return fla.get_classement(1175, saison_id=6)
    if year == '2018':
        return fla.get_classement(1146, saison_id=5)
    return fla.get_classement(1192, saison_id=7)

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/lesfous/www/src/static')

@route('/opponents')
@view('src/opponents.html')
def opponents():
    return fla.fetch_opponents()
