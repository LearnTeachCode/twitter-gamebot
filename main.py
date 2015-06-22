import os
import time
import sqlite3
from twython import Twython
import apikeys as keys

def sqlStart():
	return sqlite3.connect('games.db')
	
def sqlConnection(sqlconn):
	return sqlconn.cursor()

def sqlClose(conn):
	conn.close()

def filterSQLResult(string):
	string = string.split("delimiter")
	return string[1]#whatever you want to do


if __name__ == "__main__":

	twitter = Twython(
		app_key = keys.CONSUMER_KEY,
		app_secret = keys.CONSUMER_SECRET,
		oauth_token = keys.OAUTH_TOKEN,
		oauth_token_secret = keys.OAUTH_TOKEN_SECRET
		)
		
	conn = sqlStart()
	c = sqlConnection(conn)
	
	#actions to do 