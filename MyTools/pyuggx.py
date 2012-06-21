#encoding:utf-8

import sqlite3
import time
import sys

reload(sys)
print("reload")
sys.setdefaultencoding('utf-8')

def connect():        
    global conn, cur
    conn = sqlite3.connect('pinyinuggx.sqlite')
    cur = conn.cursor()


def query(val):
	if len(val) == 1:
		sql = "select * from pinyinuggx where pinyin = '" + val[0] + "' or cc = '" + val[0] + "' order by uggx"
	elif len(val) == 2:
		#第一个字母是val[1]的。
		sql = "select * from pinyinuggx where pinyin = '" + val[0] + "' and uggx like '" + val[1] + "%' order by uggx"
		print (sql)
	cur.execute(sql)
	
	res = cur.fetchall()
	
	return res


def close():
	conn.close()

	
def go():
	hint = 'Please input pinyin n > '
	sea = raw_input(hint)
	#sea = sea.lower()
	sea = sea.split()
	
	connect()

	res = query(sea)
	#res 0 1 2 3

	finalstr = "" 

	for r in res:
		finalstr = finalstr + "\n" + r[2] + "  " + r[1] + "  " + r[3]
		
	if ("" == finalstr):
		finalstr = "Sorry, no '" + str(sea) + "' found!\nWe might not have this in our database.\n"
	
	print (finalstr)
	finalstr = unicode(finalstr)
	return finalstr

def saveToFile(args):
    f = file('pyuggxData.txt', 'a')
    f.write(args)
    print("write")
    f.close()


	
	
# Here we go
	
while (True):
	myval = go()
	saveToFile(myval)
	#ex = raw_input("\nPress Enter to go on.")





	
