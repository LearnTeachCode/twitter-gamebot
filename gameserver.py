import os, time, re, logging, requests, json
from twython import Twython
from random import randint
from pprint import pprint

def tweet(player, message):
	logging.info('tweet :: ' + player + ' :: ' + message) 

#loads the config variables from a file called config.vars
def loadConfig():
	logging.info('loadConfig :: opening config.vars')
	with open('config.vars') as conf:
		data = json.load(conf)
	return data

class player(object):
	name = ""
	attitude = ""
	apiKey = ""
	apiSecret = ""
	
	def __init__(self, cfg):
		self.name = cfg['player'][0]['name']
		self.attitude = cfg['player'][0]['attitude']
		self.apiKey = cfg['player'][0]['APP_KEY']
		self.Secret = cfg['player'][0]['APP_SECRET']

class game(object):
	gameState = {}
	playerOne = []
	#playerTwo = player("")
		
	def __init__(self, cfg):
		self.playerOne = player(cfg)	
		print self.playerOne.name
	#checks the db to see if a game is in progress
	#if it is, then it loads the current state of the game
	#into memory
	#this is going to have to be moved outside of the game class
	def checkInProgress(self):
        	logging.info('checkInProgress :: started')
        	if(True):
                	self.loadGameState()
                	self.playGame()
        	else:
                	self.startGame()

	def checkWin(self):
		logging.info('checkWin :: checking win conditions')
		return False

	#startGame picks a game from a list of available games
	#sets that game active in the db (game name, playing = true) 	
	def startGame(self):
        	loggin.info('')
        	#players = pickPlayers()
        	#setGameActive(game, players)
        	#game.setPlayes(players)

	#reads in the current state of the game into memory
	#returns the player whos turn it is next
	def loadGameState(self):
        	logging.info('loadGameState :: called')
        	self.gameState = self.getGameState()
        	self.players = self.getPlayers()

	##set and get helper methods for saving the state of the game
	##and retrieivng the state of the game
	def setPlayers(self, players):
		logging.info('setPlayers :: setting players to DB')
	
	def getPlayers(self):
		logging.info('getPlayers :: getting players from DB')

	def getGameState(self):
		logging.info('getGameState :: getting state from DB')

	def setGameState(self):
		logging.info('setGameStat :: setting state to DB')
	
	#this is the game logic
	def playGame(self):
        	logging.info('playGame :: playing')
        	
		movesList = {
				0: 'paper',
				1: 'rock',
				2: 'scissors',
		}

		player1 = randint(0,2)
		player2 = randint(0,2)		
		
		print movesList[player1]
		print movesList[player2]
                
		if (player1 == player2):
                        print "tie"
                if (player1 == 0 and player2 == 1):
                        print "player 1 winner"
                if (player1 == 0 and player2 == 2):
                        print "player 2 winner"
                if (player1 == 1 and player2 == 0):
                        print "player 2 winner"
                if (player1 == 1 and player2 == 2):
                        print "player 1 winner"
                if (player1 == 2 and player2 == 0):
                        print "player 1 winner"
                if (player1 == 2 and player2 == 1):
                        print "player 2 winner"	
		self.checkWin()

def main():
	logging.basicConfig(level=logging.INFO)
	logging.info('gameserver starting')
	cfg = loadConfig()
	
	##  gameserver()
	##  
	
	prs = game(cfg)
	prs.checkInProgress()

if __name__ == "__main__":
	main()
