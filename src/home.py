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

@route('/foot11')
@view('src/football.html')
def foot11():
    return fla.get_classement(1170)

@route('/foot7')
@view('src/football.html')
def foot7():
    return fla.get_classement(1175)

@route('/archive/foot11')
@view('src/football.html')
def archive_foot11():
    return fla.get_classement(1144, saison_id=5)

@route('/archive/foot7')
@view('src/football.html')
def archive_foot7():
    return fla.get_classement(1146, saison_id=5)
    
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/lesfous/www/src/static')
