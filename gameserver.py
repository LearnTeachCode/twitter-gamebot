import os
import time
import sqlite3
from twython import Twython
#import apikeys as keys
import logging

def sqlStart():
	logging.info('sqlStart')
	#return sqlite3.connect('games.db')
	
def sqlConnection(sqlconn):
	logging.info('sqlConnection' + " :: " + str(sqlconn))
	#return sqlconn.cursor()

def sqlClose(conn):
	logging.info('sqlClose' + " :: " + str(conn))
	#conn.close()

def filterSQLResult(string):
	logging.info('filterSQLResult' + " :: " + str(string))
	#string = string.split("delimiter")
	#return string[1]#whatever you want to do

def gameLogic():
	pass

def main():
	logging.basicConfig(level=logging.INFO)
	logging.info('gameserver starting')
	
	sqlStart()
	sqlConnection("sqlconn")
	sqlClose("conn")
	filterSQLResult("value")
	
	## to be added later
	#twitter = Twython(
	#	app_key = keys.CONSUMER_KEY,
	#	app_secret = keys.CONSUMER_SECRET,
	#	oauth_token = keys.OAUTH_TOKEN,
	#	oauth_token_secret = keys.OAUTH_TOKEN_SECRET
	#	)
		
	#conn = sqlStart()
	#c = sqlConnection(conn)                            

if __name__ == "__main__":
	main()
