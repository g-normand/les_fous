from bottle import route, run, jinja2_view as view, error, static_file
import fla

@route('/hello')
def hello():
    return "Hello World! and foxy !"

@route('/')
@view('index.html')
def index():
    return dict()

@error(500)
def error500(error):
    print(error)
    return 'Oups, une erreur est survenue'

@route('/foot11')
@view('football.html')
def foot11():
    return fla.get_classement(1170)

@route('/foot7')
@view('football.html')
def foot7():
    return fla.get_classement(1175)

@route('/archive/foot11')
@view('football.html')
def foot11():
    return fla.get_classement(1144, saison_id=5)

@route('/archive/foot7')
@view('football.html')
def foot7():
    return fla.get_classement(1146, saison_id=5)
    
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/lesfous/www/static')
