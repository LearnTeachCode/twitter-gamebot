import os
import time
import sqlite3
import re
import random
from twython import Twython
#import apikeys as keys
import logging

def sqlAuthenticate():
	#authenticate stuff

def sqlStart():
	logging.info('sqlStart')
	#return sqlite3.connect('games.db')
	
def sqlConnection(sqlconn):
	logging.info('sqlConnection' + " :: " + str(sqlconn))
	#return sqlconn.cursor()

def sqlClose(conn):
	logging.info('sqlClose' + " :: " + str(conn))
	#conn.close()

def chooseRandomGame():
	listOfGames = os.listdir("games/")
	randGame = random.choice(listOfGames)
	game = __import__(randGame)
	return game
	
def identifyGame():
	return 1#figure out which game is currently being played, sql likely

def startAIGame():
	#start a game between randomly chosen but different AI bots from a list of bots
	bot1,bot2 = random.sample(botList,2)#chooses two unique bots at random from the list of bots
	game = chooseRandomGame()
	#probably a unique game identifier should be made to figure out who is playing who
	game.play_moves() #probably have parameters here defining which player is making the move

def checkGameQueue():
	#find if any games are ongoing OR if no games are being played
	return 1

def gameLogic():
	#should a bot be playing more than one game at a time?
	if checkGameQueue():#if a game is being played
		newMoves = checkTwitterMoves()
		currentGame = identifyGame()
		currentGame.play_moves()
	else:#if no games being played
		game = chooseRandomGame()
		startAIGame()#etc. etc. 		

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
