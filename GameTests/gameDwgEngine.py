#-------------------------------------------------------------------------------------
# This file is a graphics engine being used by various python games
#-------------------------------------------------------------------------------------


import pygame
import time
import random


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

def gameCaption(caption):
    if caption == 'RPSLS':
        pygame.display.set_caption('RPSLS Game')
    if caption == 'Twitter Bot Display':
        pygame.display.set_caption('Twitter Bot Display')
    if caption == 'Tic Tac Toe':
        pygame.display.set_caption('Tic Tac Toe')

def gameEvents():
    for event in pygame.event.get():  	# this gets all events that are happening in the game 
        if event.type == pygame.QUIT:	# this is a pygame function, when someone wants to exit the game
            pygame.quit()
            quit()
		
        if event.type == pygame.KEYDOWN: 	# this is for any keypress
            if event.key == pygame.K_LEFT:	# this is the left arrow key
                x_change = -5  		        # moves to the left by 5 pixels
            if event.key == pygame.K_RIGHT:
                x_change = 5
	
        if event.type == pygame.KEYUP:	    # when a key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

    clock.tick(60)  # 60 frames per second
    
def quitEngine():
    pygame.quit()
    exit()

def displayFill():
    gameDisplay.fill(white)

def displayUpdate():
    pygame.display.update()

def displayFlip():
    pygame.display.flip()

#--------------------------------RPSLS-Game-Definitions--------------------------

player1_location = (68, 150)    # location data for player_1 image
player2_location = (185, 150)   # location data for player_2 image

# images for RPSLS game

rockImg = pygame.image.load('rock1.png')  # outside of images on purpose. weird error otherwise
SpockImg = pygame.image.load('images\Spock_test_rev05.png') # our image we will use to move
paperImg = pygame.image.load('images\paper_test_rev03.png')
lizardImg = pygame.image.load('images\lizard_test_rev03.png')
scissorsImg = pygame.image.load('images\scissors_test_rev02.png')
#--------------------------------RPSLS-Game-Functions--------------------------

def player_captions():
    font = pygame.font.SysFont(None, 25)
    captions = font.render("PLAYER 1        PLAYER 2", True, black)
    gameDisplay.blit(captions, (50, 110))
    #gameDisplay.blit(captions, (display_width/9, display_height/4))

def gameResultText(output):
    font = pygame.font.SysFont(None, 25)
    resultCaption = font.render(output, True, black)
    gameDisplay.blit(resultCaption, (10, 250))

def player1_image(player_1_img):

    if player_1_img == "rock" :
        gameDisplay.blit(rockImg, player1_location)
    elif player_1_img == "Spock" :
        gameDisplay.blit(SpockImg, player1_location)
    elif player_1_img == "paper" :
        gameDisplay.blit(paperImg, player1_location)
    elif player_1_img == "lizard" :
        gameDisplay.blit(lizardImg, player1_location)
    elif player_1_img == "scissors" :
        gameDisplay.blit(scissorsImg, player1_location)
    else :
        return "Error: Please enter rock, paper, scissors, lizard, or Spock" 
    
def player2_image(player_2_img):

    if player_2_img == "rock" :
        gameDisplay.blit(rockImg, player2_location)
    elif player_2_img == "Spock" :
        gameDisplay.blit(SpockImg, player2_location)
    elif player_2_img == "paper" :
        gameDisplay.blit(paperImg, player2_location)
    elif player_2_img == "lizard" :
        gameDisplay.blit(lizardImg, player2_location)
    elif player_2_img == "scissors" :
        gameDisplay.blit(scissorsImg, player2_location)
    else :
        return "Error: Please enter rock, paper, scissors, lizard, or Spock" 

#-------------------------Tic-Tac-Toe-Game-Definitions-------------------------

# images for tic-tac-toe game
xImg = pygame.image.load('images\X_blueBG_rev02.png')
oImg = pygame.image.load('images\O_blackBG_rev02.png')
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


#------------------------------Tic-Tac-Toe-Game-Functions-------------------------

def new_ttt_game():

    displayFill()
    pygame.draw.rect(gameDisplay, background_color, (70,50,160,160))   

    pygame.draw.line(gameDisplay, blue, (122,50), (122, 210), 5) # vertical-left
    pygame.draw.line(gameDisplay, blue, (177,50), (177, 210), 5) # vertical-right
    pygame.draw.line(gameDisplay, blue, (70,102), (230, 102), 5) # horizontal-top
    pygame.draw.line(gameDisplay, blue, (70,157), (230, 157), 5) # horizontal-bttm

    gameDisplay.blit(xImg, (85,240))        # x image for play
    gameDisplay.blit(oImg, (165,240))       # o image for play

    pygame.display.update()

    
def updateTTTGameDisplay(image, position):
    if image == 'X':
        if position == 'top_left':
            gameDisplay.blit(xImg, top_left)     
        elif position == 'top_mid':
            gameDisplay.blit(xImg, top_mid)
        elif position == 'top_right':
            gameDisplay.blit(xImg, top_right)
        elif position == 'mid_left':
            gameDisplay.blit(xImg, mid_left)
        elif position == 'center':
            gameDisplay.blit(xImg, center)
        elif position == 'mid_right':
            gameDisplay.blit(xImg, mid_right)
        elif position == 'bttm_left':
            gameDisplay.blit(xImg, bttm_left)
        elif position == 'bttm_mid':
            gameDisplay.blit(xImg, bttm_mid)
        elif position == 'bttm_right':
            gameDisplay.blit(xImg, bttm_right)
        else:
            return -1
            
    if image == 'O':
        if position == 'top_left':
            gameDisplay.blit(oImg, top_left)     
        elif position == 'top_mid':
            gameDisplay.blit(oImg, top_mid)
        elif position == 'top_right':
            gameDisplay.blit(xImg, top_right)
        elif position == 'mid_left':
            gameDisplay.blit(oImg, mid_left)
        elif position == 'center':
            gameDisplay.blit(oImg, center)
        elif position == 'mid_right':
            gameDisplay.blit(oImg, mid_right)
        elif position == 'bttm_left':
            gameDisplay.blit(oImg, bttm_left)
        elif position == 'bttm_mid':
            gameDisplay.blit(oImg, bttm_mid)
        elif position == 'bttm_right':
            gameDisplay.blit(oImg, bttm_right)
        else:
            return -1
        

    pygame.event.poll()
    pygame.display.flip()
    
def resultText(output):
    font = pygame.font.SysFont(None, 30)
    resultCaption = font.render(output, True, black)
    gameDisplay.blit(resultCaption, (10, 10))


    
    
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






