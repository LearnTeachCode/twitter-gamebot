# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


import random, time
import gameDwgEngine

player_1 = 0
player_2 = 0

def name_to_number(name):
    '''
    This function converts each name (string) for rock, paper, scissors, lizard, and Spock name
    into s number between 0 and 4. 
    '''
    
    if name == "rock" :
        return 0
    elif name == "Spock" :
        return 1
    elif name == "paper" :
        return 2
    elif name == "lizard" :
        return 3
    elif name == "scissors" :
        return 4
    else :
        return "Error: Please enter rock, paper, scissors, lizard, or Spock" 
    

def number_to_name(number):
    '''
    This function converts each number between 0 and 4 into the corresponding string
    for rock, paper, scissors-, lizard, and Spock name. 
    '''
    
    if number == 0 :
        return "rock"
    elif number == 1 :
        return "Spock"
    elif number == 2 :
        return "paper"
    elif number == 3 :
        return "lizard"
    elif number == 4 :
        return "scissors"
    else :
        return "Error: Please enter an integer from 0 through 4."

def rpsls():

    global player_1, player_2
    
    print("")  
  
    # print out the message for the player's choice
    #print ("Player chooses", player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    #player_number = name_to_number(player_choice)

    # compute random guess for player_1 and player_2 using random.randrange()
    player_1 = random.randrange(0, 5)
    player_2 = random.randrange(0, 5)
    
    # compute difference of comp_number and player_number modulo five
    winner = (player_1 - player_2) % 5

    # convert comp_number to comp_choice using the function number_to_name()
    player_1 = number_to_name(player_1)
    player_2 = number_to_name(player_2)
    
    # use if/elif/else to determine winner, print winner message
    if winner == 0 :
        output = "Player 1 and Player 2 tie!"
        print(output)
        gameDwgEngine.gameResultText(output)
        gameDwgEngine.player1_image(player_1)
        gameDwgEngine.player2_image(player_2)
    elif winner == 1 :
        output = "Player 1 wins!"
        print(output)
        gameDwgEngine.gameResultText(output)
        gameDwgEngine.player1_image(player_1)
        gameDwgEngine.player2_image(player_2)
    elif winner == 2 :
        output = "Player 1 wins!"
        print(output)
        gameDwgEngine.gameResultText(output)
        gameDwgEngine.player1_image(player_1)
        gameDwgEngine.player2_image(player_2)
    elif winner == 3 :
        output = "Player 2 wins!"
        print(output)
        gameDwgEngine.gameResultText(output)
        gameDwgEngine.player1_image(player_1)
        gameDwgEngine.player2_image(player_2)
    else :
        output = "Player 2 wins!"
        print(output)
        gameDwgEngine.gameResultText(output)
        gameDwgEngine.player1_image(player_1)
        gameDwgEngine.player2_image(player_2)

def game_loop():
    gameExit = False

    while not gameExit:

        gameDwgEngine.gameEvents()

        gameDwgEngine.displayFill()         # game background color

        #player_image(display_width/2, display_height/2)
        rpsls()
        gameDwgEngine.player_captions()
        gameDwgEngine.displayUpdate()

        time.sleep(5)
        
        #clock.tick(60)                     # 60 frames per second


##display_width = 500
##display_height = 300

gameDwgEngine.gameCaption('RPSLS Game')	    # title of the game's display

game_loop() 

gameDwgEngine.quitEngine()




