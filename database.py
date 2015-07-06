class Database:

	def sqlAuthenticate(self):
		logging.info('sqlAuthenticate')
		#authenticate stuff

	def sqlStart(self):
		logging.info('sqlStart')
		#return sqlite3.connect('games.db')
	
	def sqlConnection(self,sqlconn):
		logging.info('sqlConnection' + " :: " + str(sqlconn))
		#return sqlconn.cursor()

	def sqlClose(self,conn):
		logging.info('sqlClose' + " :: " + str(conn))
		#conn.close()
	
	def findActiveGameIDs(self):
		return 1#return game IDs or an empty list for no active games
	
	def insertNewGame(self,players,gameName):#players is a tuple of two players
		p1,p2 = players
		return 1 
	
	def insertMove(self,gameMove):
		return 1 #insert a new move from the twitter feed into the database
	
	def getGameMovesFromID(self,gameID):
		return 1 #retrieve entire list of game moves for a particular game ID, to draw a game image
	
	def getGameNameFromID(self,gameID):
		return 1 #retrieve what game is being played based on the game ID

	def getGamePlayersFromID(self,gameID):
		return 1 #retrieve names of players from a game ID
	
	def getGameStatusFromID(self,gameID):
		return 1 #if game is active or not, from a game ID