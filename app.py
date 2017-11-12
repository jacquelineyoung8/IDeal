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

@app.route('/addReview/', methods= ['GET','POST'])
def addReview():
  if request.method == 'GET':
    return render_template('index.html')

@app.route('/FAQ/', methods = ['GET'])
def faq():
  if request.method == 'GET':
    return render_template('index.html')

@app.route('/About/', methods = ['GET'])
def about():
  if request.method == 'GET':
    return render_template('index.html')

@app.route('/Tags/', methods = ['GET'])
def tags():
  if request.method == 'GET':
    return render_template('index.html')

@app.route('/welcome/static/jumbotron.css')
def send_static():
    return url_for('static', filename='jumbotron.css')


app.secret_key = 'petEqualsLoser'

if __name__ == '__main__':
  app.debug == True
  port = os.getuid()
  app.run('0.0.0.0', port)
