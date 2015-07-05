# twitter-gamebot
This is our game bot for playing games on twitter!


### A few scratch notes, please don't remove :heart:

##Overall design
The basic aim of this project is to have two AI players playing games across twitter.  The games will rotate and moves will occur every min (1440 moves per day, so each visible bot will make 720 moves).  When one game ends, another will start up.  Each bot will announce the game it's playing, the moves it makes, and some kind of visual representation of the game.  The whole thing sits on Heroku on the free tier as a scheduled task, chugging along through this sisyphean task.

#####Major components:
python 2.x
postgres (running stats, persistent game data)
heroku

#####gameserver.py

reads in the bot api keys from config.vars
makes sure it is authenticated on the twitter api :-D
checks to see if a game is in progress (postgres db: active game, moves)
if no game is playing, gameserver pulls a game from a list of available games and sets that game as being active (postgres)
players both tweet the game they're starting and their opponent
the loser of the last game starts off the new game
player 1 and 2 alternate moves until a winner is found
the game stops, the db is updated with:
	Player that won, game that was won, number of moves

#####config.vars
config.vars is a flatfile dict holding the basic game info.  copy paste this below and then plop in your api keys and whatnot. 

```python
{
        'apiKey': 'somevalue',
        'username': 'namevalue'
}
```
