# =============================================================================
#   Name:  Kenneth Perkins
#   Date:   Aug 8, 2013
#   Taken From: http://programmingnotes.freeweq.com/
#   File: memory.py
#   Description: This is the memory.py module which is the 'main' file. This
#      file utilizes the GameBoard and Music class located in "gameMusic.py" &
#      "gameBoard.py" to simulate a memory based card game where a player tries
#      to find matching pairs of the same type of card in a deck
# =============================================================================
# python3 memory.py
import pygame, sys, os
from pygame.locals import *
#from pygame._view import * # uncomment if creating a python executable
# import my own modules from the "data/libs" folder
from gameBoard import *
from gameMusic import *

# These are default attributes that will be used for the program. They're
# passed to the "gameBoard" class and can be changed in the future if so desired
TITLE_CAPTION = "Brainy Memory Game"
WINDOW_WIDTH = 760 # size of window's width in pixels
WINDOW_HEIGHT = 600 # size of window's height in pixels
NUM_PICS = 27 # total num of pics (game cards) which are in the "data/img" folder
NUM_PAIRS = 9 # total num of possible matching pairs at any given time

# ========================================
#
#              MAIN
#
# ========================================
def main():
    # variable and class declarations which are used in main
    inGame = False
    numGuesses = 0
    numPairs = 0
    SELECTION_ONE = -1
    SELECTION_TWO = -1
    clock = pygame.time
    game_Board = GameBoard()
    game_Music = Music("intro.wav","inGame.ogg","card.ogg",
        "pair.ogg","win.ogg","gameOver.ogg","noPair.ogg","helpMusic.ogg")

    # pre initialize the screen size and game board
    os.environ["SDL_VIDEO_CENTERED"] = '1' # place screen in the middle of monitor
    game_Board.InitializeScreenSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    game_Board.SetGameTitle(TITLE_CAPTION)
    game_Board.InitializeGameData(NUM_PICS)
    game_Board.RandomizeGamePieces()

    # start the intro music
    game_Music.PlayIntro()

    # this displays the initial START MENU to the screen
    while(not inGame):
        inGame = game_Board.DisplayStartScreen()
        clock.wait(70) # do this so the CPU doesnt work too hard

    # stop the intro music
    game_Music.StopIntro()

    # this is the main game loop which is the START OF THE GAME
    while(inGame):
        game_Board.DisplayIngameBackground(numGuesses, numPairs)
        game_Music.PlayInGame()

        # if the game has not ended, keep going
        if(numPairs < NUM_PAIRS):

            # display initial gameboard to screen
            if(game_Board.NumPairs() < 1):
                #print("NO MATCHES")
                game_Board.DisplayGameBoard()

            # display updated gameboard with uncovered cards
            elif(game_Board.NumPairs() > 0):
                game_Board.DisplayGameBoard()
                pygame.display.update()

                # if the user makes 2 selections, determine if they're a match
                if((SELECTION_ONE > -1) and (SELECTION_TWO > -1)):
                    #print(SELECTION_ONE)
                    #print(SELECTION_TWO)
                    clock.wait(1500)

                    # event handling loop - discard any selections
                    # the user makes while detrmining a match
                    for event in pygame.event.get():
                        if(event.type == MOUSEBUTTONUP):
                            continue
                            #print("DISCARD SELECTION")

                    # do this if they're a match
                    if(game_Board.IsPair(SELECTION_ONE, SELECTION_TWO)):
                        #print("\nMATCH\n")
                        numPairs += 1
                        game_Music.PlayPairSoundFX()

                    # do this if not a match
                    else:
                        #print("\nNOT MATCH\n")
                        game_Music.PlayNoPairSoundFX()
                        game_Board.RemoveSelection()
                        game_Board.RemoveSelection()
                    SELECTION_ONE = -1
                    SELECTION_TWO = -1

            # GET MOUSE EVENTS
            for event in pygame.event.get(): # event handling loop
                if((event.type == QUIT) or (event.type == KEYUP and event.key == K_ESCAPE)):
                    print("EXITING..")
                    inGame = False

                # get mouse motions
                if(event.type == MOUSEMOTION):
                    mouseX, mouseY = event.pos
                    #print("x = ",mouseX," y = ",mouseY)

                # get mouse clicks
                elif(event.type == MOUSEBUTTONUP):
                    mouseX, mouseY = event.pos
                    #print("MOUSE CLIKED")
                    #print("x = ",mouseX," y = ",mouseY)

                    # if the user clicks the help icon
                    if(game_Board.GetSelection(mouseX, mouseY) == "help"):
                        #print("HELP ICON")
                        game_Music.PauseInGame()
                        game_Music.PlayHelp()
                        inGame = game_Board.DisplayHelp()
                        game_Music.StopHelp()
                        game_Music.ResumeInGame()

                    # get selection for turn #1
                    elif((numGuesses % 2) == 0):
                        SELECTION_ONE = game_Board.GetSelection(mouseX, mouseY)
                        #print("TURN 1")
                        if(SELECTION_ONE > -1):
                            game_Music.PlayCardSoundFX()
                            game_Board.AppendSelection(SELECTION_ONE)
                            numGuesses += 1
                    # get selection for turn #2
                    else:
                        SELECTION_TWO = game_Board.GetSelection(mouseX, mouseY)
                        #print("TURN 2")
                        if(SELECTION_TWO > -1):
                            game_Music.PlayCardSoundFX()
                            game_Board.AppendSelection(SELECTION_TWO)
                            numGuesses += 1

        # GAME IS OVER display end of game screen to user
        else:
            #print(numPairs)
            #print(game_Board.NumPairs())
            #print("NUMBER OF GUESSES = ",numGuesses/2)
            game_Board.DisplayGameBoard()
            pygame.display.update()
            clock.wait(2500)
            game_Music.StopInGame()
            game_Music.PlayWinSoundFX()
            game_Music.PlayGameOver()
            inGame = game_Board.GameOver(numGuesses)
            game_Music.StopGameOver()
            game_Board.DisplayWhiteScreen()
            game_Board.ReInitializeBoard()
            numGuesses = 0
            numPairs = 0
        pygame.display.flip()
        clock.wait(70) # do this so the CPU doesnt work too hard

    # end game if user doesnt want to play again
    print("\nThanks For Playing!!!")
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
# http://programmingnotes.freeweq.com/