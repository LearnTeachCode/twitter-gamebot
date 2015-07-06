import os, time, re, logging, requests, json
from twython import Twython
from random import randint
from pprint import pprint
from player_class import Player
from game_class import Game

class Player(object):
	name = ""
	attitude = ""
	apiKey = ""
	apiSecret = ""
	
	def __init__(self, cfg):
		self.name = cfg['player'][0]['name']
		self.attitude = cfg['player'][0]['attitude']
		self.apiKey = cfg['player'][0]['APP_KEY']
		self.Secret = cfg['player'][0]['APP_SECRET']

