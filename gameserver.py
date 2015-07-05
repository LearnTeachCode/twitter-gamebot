import os
import time
import sqlite3
import re
import random
from twython import Twython
#import apikeys as keys
import logging

########################################################
##################    SQL CODE     #####################
########################################################

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
	
def findActiveGameIDs():
	return 1#return game IDs or an empty list for no active games
	
def insertNewGame(players,gameName):#players is a tuple of two players
	p1,p2 = players
	return 1 
	
def insertMove(gameMove):
	return 1 #insert a new move from the twitter feed into the database
	
def getGameMovesFromID(gameID):
	return 1 #retrieve entire list of game moves for a particular game ID, to draw a game image
	
def getGameNameFromID(gameID):
	return 1 #retrieve what game is being played based on the game ID

def getGamePlayersFromID(gameID):
	return 1 #retrieve names of players from a game ID
	
def getGameStatusFromID(gameID):
	return 1 #if game is active or not, from a game ID
	
########################################################
##################    SQL CODE     #####################
########################################################


def chooseRandomGame():
	listOfGames = os.listdir("games/")
	randGame = random.choice(listOfGames)
	game = __import__('games/'+randGame)#import the game module
	return game

def startBotGame():
	#start a game between randomly chosen but different AI bots from a list of bots
	bot1,bot2 = random.sample(botList,2)#chooses two unique bots at random from the list of bots
	game = chooseRandomGame()
	#probably a unique game identifier should be made to figure out who is playing who
	game.play_moves() #probably have parameters here defining which player is making the move

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
