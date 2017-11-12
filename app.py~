from flask import Flask, render_template, request, flash, url_for
import os, sys
import MySQLdb
import dbconn2

app = Flask(__name__)

def getConn():
  DSN = dbconn2.read_cnf()
  DSN['db'] = 'bramanud_db' #LOSER
  return dbconn2.connect(DSN)

@app.route('/welcome/', methods = ['GET'])
def welcome():
  if request.method == 'GET':
    return render_template('index.html')
# @app.route('/css/', methods = ['GET'])
# def appPage():
#   return app.send_static_file("src/x-app.html")
#@app.route('/addReview/', methods= ['GET','POST'])
#@app.route('/FAQ/', methods = ['GET'])
#@app.route('/About/', methods = ['GET'])
#@app.route('/Tags/', methods = ['GET'])


@app.route('/welcome/static/jumbotron.css')
def send_static():
    return url_for('static', filename='jumbotron.css')


app.secret_key = 'nancyEqualsLoser'

if __name__ == '__main__':
  app.debug == True
  port = os.getuid()
  app.run('0.0.0.0', port)
