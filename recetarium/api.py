import bottle
from bottle import run

if __name__ == "__main__":
    run(host='127.0.0.0', port='8000', debug=False, reloader=True)