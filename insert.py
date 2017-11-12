#insert script


import dbconn2 
import MySQLdb
import pandas as pd
import re

def getConn():
	DSN = dbconn2.read_cnf()
	DSN['db'] = 'bramanud_db' #LOSER
	return dbconn2.connect(DSN)
conn = getConn()
curs = conn.cursor(MySQLdb.cursors.DictCursor)

df = pd.read_csv("data.csv")

def removeChar(string):
	# regex = re.compile('[^a-zA-Z]')
	return re.sub(r'([^\s\w]|_)+', '', string)

df['Review Text'] = df['Review Text'].apply(lambda x: removeChar(x))
df['Job Title'].fillna('Unknown', inplace= True)
df['Positive/Negative'].fillna('0', inplace= True)
tuples = []
i = 1
for index, row in df.iterrows():
	tuples.append((str(i), row['Company'], row['Review Text'], row['Positive/Negative'], row['Job Title']))
	i += 1

def exists(key):
	curs.execute('select * from companies where c_name = %s', (key,))
	print "IN EXISTS"
	row = curs.fetchone()
	return (row is not None)

def add():
	#tuples is a list of the tuples to insert
	count = 0
	while count < len(tuples):
		tup = tuples[count]
		key = tup[1]
		if (not exists(key)):
			curs.execute("insert into companies values (%s)", (tup[1],))
		curs.execute("insert into reviews values (%s, %s, %s, %s, %s)",
			(tup[0], tup[1], tup[2], tup[3], tup[4]))
		count += 1
add()





