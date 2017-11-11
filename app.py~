from flask import flask
import os, sys
import MySQLdb
import dbconn2

app = Flask(__name__)

def getConn():
  DSN = dbconn2.read_cnf()
  DSN['db'] = 'nho_db' #LOSER
  return dbconn2.connect(DSN)

@app.route('/welcome/', methods = ['GET'])
def welcomePage():
  return render_template("index.html")

@app.route('/addReview/', methods= ['GET','POST'])
@app.route('/FAQ/', methods = ['GET'])
@app.route('/About/', methods = ['GET'])
@app.route('/Tags/', methods = ['GET'])
