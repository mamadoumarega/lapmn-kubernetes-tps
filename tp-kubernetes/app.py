from flask import Flask, request
import datetime
import os

log_dir = os.environ['LOGDIR']
app = Flask(__name__)

@app.route('/')
def index():
    """default route"""
    return "Hello world !"

@app.route('/log')
def log():
    """renvoyer le contenu du fichier de logs"""
    fh = open(log_dir + '/journal.log', 'r')
    return fh.read()

@app.route('/post')
def post():
    """ajouter une IP et la date dans un fichier"""
    now = datetime.datetime.now()
    fh = open(log_dir + '/journal.log', 'a')
    info = "{} - {}\n".format(str(now), request.remote_addr)
    fh.write(info)
    fh.close()
    return info

if __name__ == "__main__":
    app.run(host='0.0.0.0')
