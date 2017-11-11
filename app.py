from flask import Flask
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
  return curent_app.send_static_file("index.html")

#@app.route('/addReview/', methods= ['GET','POST'])
#@app.route('/FAQ/', methods = ['GET'])
#@app.route('/About/', methods = ['GET'])
#@app.route('/Tags/', methods = ['GET'])

app.secret_key = 'petEqualsLoser'

if __name__ == '__main__':
  app.debug == True
  port = os.getuid()
  app.run('0.0.0.0', port)
