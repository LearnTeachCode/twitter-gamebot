import random
import sqlite3
import time
import gameDwgEngine



class Tic_Tac_Toe_game(object):
    '''
    This sets up a tic-tac-toe (ttt) game between two human players
    The ttt grid is represented in a 2D list.
    '''

    def __init__(self, game_ID):
        
        self.game_list = [['-','-','-'],['-','-','-'],['-','-','-']]  # initialize 2D array for empty tic-tac-toe game
        self.game_ID = game_ID
        print("Game_ID: %s - " % (self.game_ID))
        print('')

    def game_as_dict(self, game = 0):

        self.game_dict = {"top_left": '-', "mid_left": '-', "bttm_left": '-', "top_mid": '-', "center": '-', "bttm_mid": '-', "top_right": '-', "mid-right": '-', "bttm_right": '-'}
        print(game_dict)
        print('')
                 
    def ttt_game(self, **kwargs):
        
        print(kwargs)

    def set_new_game(self):
        
        self.game_list = [['-','-','-'],['-','-','-'],['-','-','-']]
        

    def print_ttt_grid(self):
        
        i = 0
        while i < 3:
            j = 0
            while j < 3:
                #print (self.game_list[i][j],  end = '    ')    # for py v3.4
                print self.game_list[i][j], '    ',             # for py v2.7
                j += 1
            i += 1
            print('')
        print('')
    
    def ttt_gameLoop(self):

        
        count = 0       # keep track of games played for session for this game_ID
        
        gameExit = True
        while gameExit:
            if count == 0:      # first ttt game being played
                #start_playing = input("Do you want to play Tic-Tac-Toe? - Type yes or no: ").lower()
                start_playing = raw_input("Do you want to play Tic-Tac-Toe? - Type yes or no: ").lower()
                print('')
            else:
                #start_playing = input("Play again? - Type yes or no: ").lower()
                start_playing = raw_input("Play again? - Type yes or no: ").lower()
                print('')
            if start_playing == ('n' or 'no'):
                print('Goodbye')
                break
            elif len(start_playing) < 1: break      # check for empty line
            elif start_playing == ('y' or 'yes'):
                gameExit = False
                player_choice = None
                print('')
                print("The valid moves are:\n")
                print("top left       top middle     top right\n")
                print("middle left      center       middle right\n")
                print("bottom left   bottom middle   bottom left\n")
            else:
                gameDwgEngine.quitEngine()

            
            gameDwgEngine.new_ttt_game()
            self.set_new_game()
            
        
            count += 1
            totalMoves = 9      # total # of moves possible per game
            while not gameExit:
                """
                for event in pygame.event.get():  	# this gets all events that are happening in the game 
                    if event.type == pygame.QUIT:	# this is a pygame function, when someone wants to exit the game
                        pygame.quit()
                        quit()
                """
                
                gameDwgEngine.displayUpdate()

                if player_choice == None:
                    #player_choice = input("Pick X or O: ").upper()
                    player_choice = raw_input("Pick X or O: ").upper()
                if player_choice == 'X':
                    #player_X = input("Make your move X player: ")
                    player_X = raw_input("Make your move X player: ")
                    print('')
                elif player_choice == 'O':
                    #player_O = input("Make your move O player: ")
                    player_O = raw_input("Make your move O player: ")
                    print('')
                else:
                    print("Sorry you don't feel like playing")
                    gameDwgEngine.quitEngine()
                    
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
                                gameDwgEngine.updateTTTGameDisplay('X', 'top_left')
                            else:
                                print("That move was taken. Try again please")
                                #player_X = input("Make your move X player: ")
                                player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "top middle") or (player_X == "top mid") or (player_X == "tm") or (player_X == "8")):
                            if (self.game_list[0][1] != ('X' or 'O')):
                                self.game_list[0][1] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('X', 'top_mid')
                            else:
                                print("That move was taken. Try again please")
                                #player_X = input("Make your move X player: ")
                                player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "top right") or (player_X == "tr") or (player_X == "9")):
                            if (self.game_list[0][2] != ('X' or 'O')):
                                self.game_list[0][2] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('X', 'top_right')
                            else:
                                print("That move was taken. Try again please")
                                #player_X = input("Make your move X player: ")
                                player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "middle left") or (player_X == "mid left") or (player_X == "ml") or (player_X == "4")):
                            if (self.game_list[1][0] != ('X' or 'O')):
                                self.game_list[1][0] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('X', 'mid_left')
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
                                gameDwgEngine.updateTTTGameDisplay('X', 'center')
                            else:
                                print("That move was taken. Try again please")
                                #player_X = input("Make your move X player: ")
                                player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "middle right") or (player_X == "mid right") or (player_X == "mr") or (player_X == "6")):
                            if (self.game_list[1][2] != ('X' or 'O')):
                                self.game_list[1][2] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('X', 'mid_right')
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
                                gameDwgEngine.updateTTTGameDisplay('X', 'bttm_left')
                            else:
                                print("That move was taken. Try again please")
                                #player_X = input("Make your move X player: ")
                                player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "bottom middle") or (player_X == "bottom mid") or (player_X == "bm") or (player_X == "2")):
                            if (self.game_list[2][1] != ('X' or 'O')):
                                self.game_list[2][1] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('X', 'bttm_mid')
                            else:
                                print("That move was taken. Try again please")
                                #player_X = input("Make your move X player: ")
                                player_X = raw_input("Make your move X player: ")
                                numOfAttempts -= 1
                        elif ((player_X == "bottom right") or (player_X == "br") or (player_X == "3")):
                            if (self.game_list[2][2] != ('X' or 'O')):
                                self.game_list[2][2] = 'X'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('X', 'bttm_right')
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
                            #player_X = input("Make your move X player: ")
                            player_X = raw_input("Make your move X player: ")
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
                                gameDwgEngine.updateTTTGameDisplay('O', 'top_left')
                            else:
                                print("That move was taken. Try again please")
                                #player_O = input("Make your move O player: ")
                                player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1    
                        elif ((player_O == "top middle") or (player_O == "top mid") or (player_O == "tm") or (player_O == "8")):
                            if (self.game_list[0][1] != ('X' or 'O')):
                                self.game_list[0][1] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('O', 'top_mid')
                            else:
                                print("That move was taken. Try again please")
                                #player_O = input("Make your move O player: ")
                                player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "top right") or (player_O == "tr") or (player_O == "9")):
                            if (self.game_list[0][2] != ('X' or 'O')):
                                self.game_list[0][2] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('O', 'top_right')
                            else:
                                print("That move was taken. Try again please")
                                #player_O = input("Make your move O player: ")
                                player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "middle left") or (player_O == "mid left") or (player_O == "ml") or (player_O == "4")):
                            if (self.game_list[1][0] != ('X' or 'O')):
                                self.game_list[1][0] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('O', 'mid_left')
                            else:
                                print("That move was taken. Try again please")
                                #player_O = input("Make your move O player: ")
                                player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "center") or (player_O == "c") or (player_O == "5")):
                            if (self.game_list[1][1] != ('X' or 'O')):
                                self.game_list[1][1] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('O', 'center')
                            else:
                                print("That move was taken. Try again please")
                                #player_O = input("Make your move O player: ")
                                player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "middle right") or (player_O == "mid right") or (player_O == "mr") or (player_O == "6")): 
                            if (self.game_list[1][2] != ('X' or 'O')):
                                self.game_list[1][2] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('O', 'mid_right')
                            else:
                                print("That move was taken. Try again please")
                                #player_O = input("Make your move O player: ")
                                player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "bottom left") or (player_O == "bl") or (player_O == "1")):
                            if (self.game_list[2][0] != ('X' or 'O')):
                                self.game_list[2][0] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('O', 'bttm_left')
                            else:
                                print("That move was taken. Try again please")
                                #player_O = input("Make your move O player: ")
                                player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "bottom middle") or (player_O == "bottom mid") or (player_O == "bm") or (player_O == "2")):
                            if (self.game_list[2][1] != ('X' or 'O')):
                                self.game_list[2][1] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('O', 'bttm_mid')
                            else:
                                print("That move was taken. Try again please")
                                #player_O = input("Make your move O player: ")
                                player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        elif ((player_O == "bottom right") or (player_O == "br") or (player_O == "3")):
                            if (self.game_list[2][2] != ('X' or 'O')):
                                self.game_list[2][2] = 'O'
                                self.print_ttt_grid()
                                isMoveMade = True
                                totalMoves -= 1
                                gameDwgEngine.updateTTTGameDisplay('O', 'bttm_right')
                            else:
                                print("That move was taken. Try again please")
                                #player_O = input("Make your move O player: ")
                                player_O = raw_input("Make your move O player: ")
                                numOfAttempts -= 1 
                        else:
                            print("That is not a valid move. The valid moves are:\n")
                            print("top left       top middle     top right\n")
                            print("middle left      center       middle right\n")
                            print("bottom left   bottom middle   bottom left\n")
                            print("Try again please.\n")
                            #player_O = input("Make your move O player: ")
                            player_O = raw_input("Make your move O player: ")
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
                    gameDwgEngine.resultText("You Won! %s player" % self.game_list[0][0])
                    gameExit = True
                elif self.game_list[1][0] == self.game_list[1][1] == self.game_list[1][2] != '-':   # row 2
                    print("You Won! %s player" % self.game_list[1][0])
                    gameDwgEngine.resultText("You Won! %s player" % self.game_list[1][0])
                    gameExit = True
                elif self.game_list[2][0] == self.game_list[2][1] == self.game_list[2][2] != '-':   # row 3
                    print("You Won! %s player" % self.game_list[2][0])
                    gameDwgEngine.resultText("You Won! %s player" % self.game_list[2][0])
                    gameExit = True
                elif self.game_list[0][0] == self.game_list[1][0] == self.game_list[2][0] != '-':   # column 1
                    print("You Won! %s player" % self.game_list[0][0])
                    gameDwgEngine.resultText("You Won! %s player" % self.game_list[0][0])
                    gameExit = True
                elif self.game_list[0][1] == self.game_list[1][1] == self.game_list[2][1] != '-':   # column 2
                    print("You Won! %s player" % self.game_list[0][1])
                    gameDwgEngine.resultText("You Won! %s player" % self.game_list[0][1])
                    gameExit = True
                elif self.game_list[0][2] == self.game_list[1][2] == self.game_list[2][2] != '-':   # column 3
                    print("You Won! %s player" % self.game_list[0][2])
                    gameDwgEngine.resultText("You Won! %s player" % self.game_list[0][2])
                    gameExit = True
                elif self.game_list[0][0] == self.game_list[1][1] == self.game_list[2][2] != '-':   # diagonal top-left to right-bttm
                    print("You Won! %s player" % self.game_list[0][0])
                    gameDwgEngine.resultText("You Won! %s player" % self.game_list[0][0])
                    gameExit = True
                elif self.game_list[0][2] == self.game_list[1][1] == self.game_list[2][0] != '-':   # diagonal top-right to left-bttm
                    print("You Won! %s player" % self.game_list[0][2])
                    gameDwgEngine.resultText("You Won! %s player" % self.game_list[0][2])
                    gameExit = True
                else:
                    if totalMoves == 0:
                        print("It's a Tie! Game Over.")
                        gameDwgEngine.resultText("It's a Tie! Game Over.")
                        gameExit = True
                    print('')

                    
                # this toggles the player between X's and O's if game is still in progress
                if not gameExit:
                    if (player_choice == 'X'): player_choice = 'O'
                    else: player_choice = 'X'

                gameDwgEngine.displayFlip()
                #mouse = pygame.mouse.get_pos()
                #print(mouse)


  

        
gamePlay = Tic_Tac_Toe_game("#1234")
gameDwgEngine.gameCaption('Tic Tac Toe')	    # title of the game's display
#gamePlay.new_ttt_game()
gameDwgEngine.new_ttt_game()
#gamePlay.game_as_dict()
gamePlay.print_ttt_grid()
gamePlay.ttt_gameLoop()





