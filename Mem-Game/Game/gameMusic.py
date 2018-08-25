# =============================================================================
#   Name:  Kenneth Perkins
#   Date:   Aug 8, 2013
#   Taken From: http://programmingnotes.freeweq.com/
#   File: gameMusic.py
#   Description: This is the gameMusic.py module which sets up the game sounds
#      and music. This class also reads files (.ogg/.wav) from the "snd"
#      directory for use within this program. This is a memory based card game
#      where a player tries to find matching pairs of the same type of card
#      in a deck
# =============================================================================
import pygame, os
from pygame.locals import *

# game music class declaration
class Music(object):
    # this is the constructor which declares variables for use within the class
    def __init__(self, intro, game, card, pair, win, over, noPair, help):
        pygame.mixer.pre_init(44100, -16, 2)
        pygame.init()
        self.introMusic = pygame.mixer.Sound(os.path.join("data/snd/",intro))
        self.gameMusic = pygame.mixer.Sound(os.path.join("data/snd/",game))
        self.cardSoundFX = pygame.mixer.Sound(os.path.join("data/snd/",card))
        self.pairSoundFX = pygame.mixer.Sound(os.path.join("data/snd/",pair))
        self.winSoundFX = pygame.mixer.Sound(os.path.join("data/snd/",win))
        self.gameOverMusic = pygame.mixer.Sound(os.path.join("data/snd/",over))
        self.noPairSoundFX = pygame.mixer.Sound(os.path.join("data/snd/",noPair))
        self.helpMusic = pygame.mixer.Sound(os.path.join("data/snd/",help))
        self.semaphore = True # ensures only one backgroung music plays at a time
        self.clock = pygame.time

    # plays the intro (starting screen) music
    def PlayIntro(self):
        if(self.semaphore):
            self.introMusic.play(-1)
            self.semaphore = False

    # stops the intro (starting screen) music from playing
    def StopIntro(self):
        self.introMusic.stop()
        self.semaphore = True

    # plays the in game music
    def PlayInGame(self):
        if(self.semaphore):
            self.gameMusic.play(-1)
            self.semaphore = False

    # pauses the in game music from playing
    def PauseInGame(self):
        pygame.mixer.pause() # pauses ALL current sounds
        self.semaphore = True

    # resumes the in game music from playing
    def ResumeInGame(self):
        pygame.mixer.unpause()# unpauses ALL current sounds
        self.semaphore = False

    # stops the in game music from playing
    def StopInGame(self):
        self.gameMusic.stop()
        self.semaphore = True

    # plays the card soundfx music
    def PlayCardSoundFX(self):
        self.cardSoundFX.play()

    # plays the card "pair" music
    def PlayPairSoundFX(self):
        self.pairSoundFX.play()

    # plays the "no pair" music
    def PlayNoPairSoundFX(self):
        self.noPairSoundFX.play()

    # plays the "win" music
    def PlayWinSoundFX(self):
        self.winSoundFX.play()

    # plays the game over music
    def PlayGameOver(self):
        if(self.semaphore):
            self.gameOverMusic.play(-1)
            self.semaphore = False

    # stop the game over music
    def StopGameOver(self):
        self.gameOverMusic.stop()
        self.semaphore = True

    # plays the help screen music
    def PlayHelp(self):
        if(self.semaphore):
            self.helpMusic.play(-1)
            self.semaphore = False

    # stops the help screen music
    def StopHelp(self):
        self.helpMusic.stop()
        self.semaphore = True
# http://programmingnotes.freeweq.com/