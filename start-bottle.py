from bottle import Bottle, run

import src.home
run(host='localhost', port=8080, debug=True)