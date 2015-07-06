import os, time, re, logging, requests, json
from twython import Twython
from random import randint
from pprint import pprint
from player import Player
from gameserver import GameServer

def tweet(player, message):
	logging.info('tweet :: ' + player + ' :: ' + message) 

#loads the config variables from a file called config.vars
def loadConfig():
	logging.info('loadConfig :: opening config.vars')
	with open('config.vars') as conf:
		data = json.load(conf)
	return data

def main():
	logging.basicConfig(level=logging.INFO)
	logging.info('gameserver starting')
	cfg = loadConfig()
	
	#gameserver
	
	prs = GameServer(cfg)
	prs.checkInProgress()

if __name__ == "__main__":
	main()
