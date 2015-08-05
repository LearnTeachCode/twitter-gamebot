import pygame
import time
import random
import sqlite3
import time

pygame.init()		# this line must be in all programs using the pygame module

display_width = 300
display_height = 300

# colors are described in a tuple in an RGB format
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

background_color = (235, 235, 230)      # light gray - #EBEBE6


gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(white)

pygame.display.set_caption('Twitter Bot Display')	# title of the game

clock = pygame.time.Clock()  	                        # your main game clock

#carImg = pygame.image.load('racecar.png') 	        # our image we will use to move




'''
#---------------RPSLS-Game-----------------

# images for RPSLS game
spockImg = pygame.image.load('Spock_icon')
paperImg = pygame.image.load('paper_icon')
rockImg = pygame.image.load('rock_icon')
lizardImg = pygame.image.load('lizard_icon')
scissorsImg = pygame.image.load('scissors_icon')
'''


#---------------Tic-Tac-Toe-Game-----------------

# images for tic-tac-toe game
xImg = pygame.image.load('X_blueBG_rev02.png')
oImg = pygame.image.load('O_blackBG_rev02.png')
#gridImg = pygame.image.load(' ')

#tic_tac_toeDisplay = pygame.display.set_mode((160, 160))
#pygame.draw.rect(gameDisplay, red, (50,50,160,160))  # used this to check clearances on the ttt grid

# tic-tac-toe play area
pygame.draw.rect(gameDisplay, background_color, (70,50,160,160))

'''
# the following are the insertion points for the X and O images
top_left = (50,50)
mid_left = (50,105)
bttm_left = (50,160)
top_mid = (105,50)
center = (105,105)
bttm_mid = (105,160)
top_right = (160,50)
mid_right = (160,105)
bttm_right = (160,160)
'''

# the following are the insertion points for the X and O images -> shifted right +20px
top_left = (70,50)
mid_left = (70,105)
bttm_left = (70,160)
top_mid = (125,50)
center = (125,105)
bttm_mid = (125,160)
top_right = (180,50)
mid_right = (180,105)
bttm_right = (180,160)

class Tic_Tac_Toe_game(object):
    '''
    This sets up a tic-tac-toe (ttt) game between two human players
    The ttt grid is represented in a 2D list.
    '''

    def __init__(self, game_ID):
        
        self.game_list = [['-','-','-'],['-','-','-'],['-','-','-']]  # initialize 2D array for empty tic-tac-toe game
        self.game_ID = game_ID
        print("Game_ID: %s - " % (self.game_ID))
        print()

    def game_as_dict(self, game = 0):

        self.game_dict = {"top_left": '-', "mid_left": '-', "bttm_left": '-', "top_mid": '-', "center": '-', "bttm_mid": '-', "top_right": '-', "mid-right": '-', "bttm_right": '-'}
        print(game_dict)
        print()
                 
    def ttt_game(self, **kwargs):
        
        print(kwargs)

    def new_ttt_game(self):

        pygame.draw.rect(gameDisplay, background_color, (70,50,160,160))   

        pygame.draw.line(gameDisplay, blue, (122,50), (122, 210), 5) # vertical-left
        pygame.draw.line(gameDisplay, blue, (177,50), (177, 210), 5) # vertical-right
        pygame.draw.line(gameDisplay, blue, (70,102), (230, 102), 5) # horizontal-top
        pygame.draw.line(gameDisplay, blue, (70,157), (230, 157), 5) # horizontal-bttm

        gameDisplay.blit(xImg, (85,240))        # x image for play
        gameDisplay.blit(oImg, (165,240))       # o image for play

        pygame.display.update()

        self.game_list = [['-','-','-'],['-','-','-'],['-','-','-']]

    def print_ttt_grid(self):
        
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                print(self.game_list[i][j], end='    ')
                j += 1
            i += 1
            print()
        print()
    
    def ttt_gameLoop(self):

        pygame.display.flip()
        count = 0       # keep track of games played for session for this game_ID
        
        gameExit = True
        while gameExit:
            if count == 0:      # first ttt game being played
                start_playing = input("Do you want to play Tic-Tac-Toe? - Type yes or no: ").lower()
                #start_playing = raw_input("Do you want to play Tic-Tac-Toe? - Type yes or no: ").lower()
                print()
            else:
                start_playing = input("Play again? - Type yes or no: ").lower()
                #start_playing = raw_input("Play again? - Type yes or no: ").lower()
                print()
            if start_playing == ('n' or 'no'):
                print('Goodbye')
                break
            elif len(start_playing) < 1: break      # check for empty line
            elif start_playing == ('y' or 'yes'):
                gameExit = False
                player_choice = None
                print()
                print("The valid moves are:\n")
                print("top left       top middle     top right\n")
                print("middle left      center       middle right\n")
                print("bottom left   bottom middle   bottom left\n")
            else:
                pygame.quit()
                exit()

            gamePlay.new_ttt_game()
        
            count += 1
            totalMoves = 9      # total # of moves possible per game
            while not gameExit:
                """
                for event in pygame.event.get():  	# this gets all events that are happening in the game 
                    if event.type == pygame.QUIT:	# this is a pygame function, when someone wants to exit the game
                        pygame.quit()
                        quit()
                """
                pygame.display.update()

                if player_choice == None:
                    player_choice = input("Pick X or O: ").upper()
                    #player_choice = raw_input("Pick X or O: ").upper()
                if player_choice == 'X':
                    player_X = input("Make your move X player: ")
                    #player_X = raw_input("Make your move: ")
                    print()
                elif player_choice == 'O':
                    player_O = input("Make your move O player: ")
                    #player_O = raw_input("Make your move: ")
                    print()
                else:
                    print("Sorry you don't feel like playing")
                    pygame.quit()
                    quit()
                    
                isMoveMade = False
                numOfAttempts = 7
                if player_choice == 'X':
                    while not isMoveMade:   
                        if ((player_X == "top left") or (player_X == "tl") or (player_X == "7")):
                            if (self.game_list[0][0] != ('X' or 'O')):
                                self.game_list[0][0] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(xImg, top_left)     # top_left
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_X = input("Make your move X player: ")
                                #player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "top middle") or (player_X == "top mid") or (player_X == "tm") or (player_X == "8")):
                            if (self.game_list[0][1] != ('X' or 'O')):
                                self.game_list[0][1] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(xImg, top_mid)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_X = input("Make your move X player: ")
                                #player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "top right") or (player_X == "tr") or (player_X == "9")):
                            if (self.game_list[0][2] != ('X' or 'O')):
                                self.game_list[0][2] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(xImg, top_right)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_X = input("Make your move X player: ")
                                #player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "middle left") or (player_X == "mid left") or (player_X == "ml") or (player_X == "4")):
                            if (self.game_list[1][0] != ('X' or 'O')):
                                self.game_list[1][0] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(xImg, mid_left)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_X = input("Make your move X player: ")
                                #player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "center") or (player_X == "c") or (player_X == "5")):
                            if (self.game_list[1][1] != ('X' or 'O')):
                                self.game_list[1][1] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(xImg, center)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_X = input("Make your move X player: ")
                                #player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "middle right") or (player_X == "mid right") or (player_X == "mr") or (player_X == "6")):
                            if (self.game_list[1][2] != ('X' or 'O')):
                                self.game_list[1][2] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(xImg, mid_right)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_X = input("Make your move X player: ")
                                #player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "bottom left") or (player_X == "bl") or (player_X == "1")):
                            if (self.game_list[2][0] != ('X' or 'O')):
                                self.game_list[2][0] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(xImg, bttm_left)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_X = input("Make your move X player: ")
                                #player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "bottom middle") or (player_X == "bottom mid") or (player_X == "bm") or (player_X == "2")):
                            if (self.game_list[2][1] != ('X' or 'O')):
                                self.game_list[2][1] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(xImg, bttm_mid)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_X = input("Make your move X player: ")
                                #player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "bottom right") or (player_X == "br") or (player_X == "3")):
                            if (self.game_list[2][2] != ('X' or 'O')):
                                self.game_list[2][2] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(xImg, bttm_right)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_X = input("Make your move X player: ")
                                #player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        else:
                            print("That is not a valid move. The valid moves are:\n")
                            print("top left       top middle     top right\n")
                            print("middle left      center       middle right\n")
                            print("bottom left   bottom middle   bottom left\n")
                            print("Try again please.\n")
                            player_X = input("Make your move X player: ")
                            #player_X = raw_input("Make your move X player: ")
                            numOfAttempts -= 1
                            #print("\nYou have %i attempts left." % numOfAttempts)

                        if numOfAttempts < 1:
                            print("You are not even trying! Goodday!")
                            time.sleep(4)
                            print("I said...GOODDAY!\n")
                            exit()
                            

                if player_choice == 'O':
                    while not isMoveMade:
                        if ((player_O == "top left") or (player_O == "tl") or (player_O == "7")):
                            if (self.game_list[0][0] != ('X' or 'O')):
                                self.game_list[0][0] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(oImg, top_left)     # top_left
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_O = input("Make your move O player: ")
                                #player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1    
                        elif ((player_O == "top middle") or (player_O == "top mid") or (player_O == "tm") or (player_O == "8")):
                            if (self.game_list[0][1] != ('X' or 'O')):
                                self.game_list[0][1] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(oImg, top_mid)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_O = input("Make your move O player: ")
                                #player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "top right") or (player_O == "tr") or (player_O == "9")):
                            if (self.game_list[0][2] != ('X' or 'O')):
                                self.game_list[0][2] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(oImg, top_right)     
                                pygame.event.poll()
                                pygame.display.flip()                                             
                            else:
                                print("That move was taken. Try again please")
                                player_O = input("Make your move O player: ")
                                #player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "middle left") or (player_O == "mid left") or (player_O == "ml") or (player_O == "4")):
                            if (self.game_list[1][0] != ('X' or 'O')):
                                self.game_list[1][0] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(oImg, mid_left)    
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_O = input("Make your move O player: ")
                                #player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "center") or (player_O == "c") or (player_O == "5")):
                            if (self.game_list[1][1] != ('X' or 'O')):
                                self.game_list[1][1] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(oImg, center)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_O = input("Make your move O player: ")
                                #player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "middle right") or (player_O == "mid right") or (player_O == "mr") or (player_O == "6")): 
                            if (self.game_list[1][2] != ('X' or 'O')):
                                self.game_list[1][2] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(oImg, mid_right)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_O = input("Make your move O player: ")
                                #player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "bottom left") or (player_O == "bl") or (player_O == "1")):
                            if (self.game_list[2][0] != ('X' or 'O')):
                                self.game_list[2][0] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(oImg, bttm_left)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_O = input("Make your move O player: ")
                                #player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "bottom middle") or (player_O == "bottom mid") or (player_O == "bm") or (player_O == "2")):
                            if (self.game_list[2][1] != ('X' or 'O')):
                                self.game_list[2][1] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(oImg, bttm_mid)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_O = input("Make your move O player: ")
                                #player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "bottom right") or (player_O == "br") or (player_O == "3")):
                            if (self.game_list[2][2] != ('X' or 'O')):
                                self.game_list[2][2] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDisplay.blit(oImg, bttm_right)     
                                pygame.event.poll()
                                pygame.display.flip()
                            else:
                                print("That move was taken. Try again please")
                                player_O = input("Make your move O player: ")
                                #player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        else:
                            print("That is not a valid move. The valid moves are:\n")
                            print("top left       top middle     top right\n")
                            print("middle left      center       middle right\n")
                            print("bottom left   bottom middle   bottom left\n")
                            print("Try again please.\n")
                            player_O = input("Make your move O player: ")
                            #player_O = raw_input("Make your move O player: ")
                            numOfAttempts -= 1
                            #print("\nYou have %i attempts left." % numOfAttempts)
                            
                        if numOfAttempts < 1:
                            print("You are not even trying! Goodday!")
                            time.sleep(4)
                            print("I said...GOODDAY!\n")
                            exit()
                             
                            

                # Check for a win
                if self.game_list[0][0] == self.game_list[0][1] == self.game_list[0][2] != '-':     # row 1
                    print("You Won! %s player" % self.game_list[0][0])
                    gameExit = True
                elif self.game_list[1][0] == self.game_list[1][1] == self.game_list[1][2] != '-':   # row 2
                    print("You Won! %s player" % self.game_list[1][0]) 
                    gameExit = True
                elif self.game_list[2][0] == self.game_list[2][1] == self.game_list[2][2] != '-':   # row 3
                    print("You Won! %s player" % self.game_list[2][0]) 
                    gameExit = True
                elif self.game_list[0][0] == self.game_list[1][0] == self.game_list[2][0] != '-':   # column 1
                    print("You Won! %s player" % self.game_list[0][0]) 
                    gameExit = True
                elif self.game_list[0][1] == self.game_list[1][1] == self.game_list[2][1] != '-':   # column 2
                    print("You Won! %s player" % self.game_list[0][1]) 
                    gameExit = True
                elif self.game_list[0][2] == self.game_list[1][2] == self.game_list[2][2] != '-':   # column 3
                    print("You Won! %s player" % self.game_list[0][2]) 
                    gameExit = True
                elif self.game_list[0][0] == self.game_list[1][1] == self.game_list[2][2] != '-':   # diagonal top-left to right-bttm
                    print("You Won! %s player" % self.game_list[0][0]) 
                    gameExit = True
                elif self.game_list[0][2] == self.game_list[1][1] == self.game_list[2][0] != '-':   # diagonal top-right to left-bttm
                    print("You Won! %s player" % self.game_list[0][2]) 
                    gameExit = True
                else:
                    if totalMoves == 0:
                        print("It's a Tie! Game Over.")
                        gameExit = True
                    print()

                    
                # this toggles the player between X's and O's if game is still in progress
                if not gameExit:
                    if (player_choice == 'X'): player_choice = 'O'
                    else: player_choice = 'X'

                pygame.display.flip()
                #mouse = pygame.mouse.get_pos()
                #print(mouse)


  

        
        
"""
# X-O placements
gameDisplay.blit(xImg, (50,50))     # top_left
gameDisplay.blit(xImg, (50,105))    # mid_left
gameDisplay.blit(oImg, (50,160))    # bttm_left

gameDisplay.blit(oImg, (105,50))    # top_mid
gameDisplay.blit(xImg, (105,105))   # center
gameDisplay.blit(oImg, (105,160))   # bttm_mid

gameDisplay.blit(oImg, (160,50))    # top_right
gameDisplay.blit(oImg, (160,105))   # mid_right
gameDisplay.blit(xImg, (160,160))   # bttm_right

"""
"""
# X-O placements
##gameDisplay.blit(xImg, top_left)     # top_left
gameDisplay.blit(xImg, mid_left)    # mid_left
##gameDisplay.blit(oImg, bttm_left)    # bttm_left
##
##gameDisplay.blit(oImg, top_mid)    # top_mid
gameDisplay.blit(xImg, center)   # center
##gameDisplay.blit(oImg, bttm_mid)   # bttm_mid
##
##gameDisplay.blit(oImg, top_right)    # top_right
##gameDisplay.blit(oImg, mid_right)   # mid_right
##gameDisplay.blit(xImg, bttm_right)   # bttm_right
"""

# tic-tac-toe grid lines
##pygame.draw.line(gameDisplay, blue, (102,50), (102, 210), 5) # vertical-left
##pygame.draw.line(gameDisplay, blue, (157,50), (157, 210), 5) # vertical-right
##pygame.draw.line(gameDisplay, blue, (50,102), (210, 102), 5) # horizontal-top
##pygame.draw.line(gameDisplay, blue, (50,157), (210, 157), 5) # horizontal-bttm
##
##pygame.draw.line(gameDisplay, blue, (122,50), (122, 210), 5) # vertical-left
##pygame.draw.line(gameDisplay, blue, (177,50), (177, 210), 5) # vertical-right
##pygame.draw.line(gameDisplay, blue, (70,102), (230, 102), 5) # horizontal-top
##pygame.draw.line(gameDisplay, blue, (70,157), (230, 157), 5) # horizontal-bttm
##
##gameDisplay.blit(xImg, (85,240))        # x image for play
##gameDisplay.blit(oImg, (165,240))       # o image for play
##
##
##pygame.display.update()


gamePlay = Tic_Tac_Toe_game("#1234")

gamePlay.new_ttt_game()
#gamePlay.game_as_dict()
gamePlay.print_ttt_grid()
gamePlay.ttt_gameLoop()



"""
gameExit = False
while not gameExit:

    
    
    for event in pygame.event.get():  	# this gets all events that are happening in the game 
        if event.type == pygame.QUIT:	# this is a pygame function, when someone wants to exit the game
            pygame.quit()
            quit()

    pygame.display.update()

"""   
"""
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))
	
def things(thingx, thingy, thingw, thingh, color):	# the blocks x, y, width, and height, and last the color of the block (rectangle)
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

    
def car(x,y):
    gameDisplay.blit(carImg, (x,y))		        # note (x,y) is a tuple

	
def text_objects(text, font):
    textSurface = font.render(text, True, black)	# here the font is rendered
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)	# 115 is the font size
    TextSurf, TextRect = text_objects(text, largeText)		# TextSurf is the text surface, TextRect is the rectangle placed around the text block
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
	
    pygame.display.update()
	
    time.sleep(2)		# this is how long the message is displayed on the screen  (2 seconds)
	
    game_loop()
	
	
def crash():	# this function will give instructions when a person crashes into the wall
    message_display("You Crashed")


def game_loop():
	
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
	
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600 
    thing_speed = 4 
    thing_width = 100 
    thing_height = 100

    dodged = 0 
	
    # the following is your main game loop - the logic for your game
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():  	# this gets all events that are happening in the game 
            if event.type == pygame.QUIT:	# this is a pygame function, when someone wants to exit the game
                pygame.quit()
                quit()
		
            if event.type == pygame.KEYDOWN: 	# this is for any keypress
                if event.key == pygame.K_LEFT:	# this is the left arrow key
                    x_change = -5  		# moves to the left by 5 pixels
                if event.key == pygame.K_RIGHT:
                    x_change = 5
				
				
            if event.type == pygame.KEYUP:	# when a key is released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                     x_change = 0	        # when the left or right arrow keys are released, stop the movement
				
        x += x_change	                        # this will update the location of the x location of the image
	
        #gameDisplay.fill(white) 	        # this is for making the background, make sure this is called BEFORE you place the car image code
        #gameDisplay.fill(black)     #TEST
		
	# things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed		# each time we loop we will add 7 pixels to the thing_starty position
		
        car(x,y)
        things_dodged(dodged)
		
        if x > display_width - car_width or x < 0:
            crash()
            # gameExit = True		        # if your car touches your left or right wall, then game over.
		
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)       # should have made the box wider to increase the difficulty 
			

        if y < thing_starty + thing_height:
            print("y crossover")
			
        if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
            print('x crossover')
            crash()
				
				
			
        pygame.display.update() 	# this only updates what is put in the parenthesis which is less processing, if nothing is put in the () - the entire display is updated	
                                        # you could also use pygame.display.flip() - this will update the entire display - not sure about flip() and what the difference is 
								
        clock.tick(60)		        # the number entered in () is the frame per second, here is 60FPS, this is also how fast you will run for the entire game

game_loop()


pygame.quit()	# in order to stop the pygame event
quit()
"""

