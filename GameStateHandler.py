# Description: The Game state handler for the python Depth Game
# Created By: Jacob Maughan

# Imports
from ObjectHandler import ObjectHandler
from EventHandler import EventHandler
from MapHandler import MapHandler
from Enums import GameState
from Enums import PlayerType
from Enums import UI
from Player import Player
from Weapon import Weapon
from UI import UIBar
from MainMenuObject import MainMenu

import pygame

class GameStateHandler:

    def __init__(self, window, game):
        self.window = window
        self.game = game
        self.screen = window.screen
        self.state = GameState.MAIN_MENU
        self.eventHandler = EventHandler(self.game)
        self.objectHandler = ObjectHandler()
        self.mapHandler = MapHandler(self.window)
        self.loadMenu()

    def tick(self):
        self.eventHandler.tick(self)
        if self.state == GameState.GAME:
            self.objectHandler.tick(self)

    def render(self):
        if self.state == GameState.MAIN_MENU:
            self.objectHandler.render(self.screen)
        elif self.state == GameState.GAME:
            self.mapHandler.render()
            self.objectHandler.render(self.screen)
        elif self.state == GameState.GAME_SHOP:
            print('Shop')
        elif self.state == GameState.GAME_OVER:
            screen = pygame.image.load('./assets/GameOver.png')
            screen = pygame.transform.scale(screen, (self.window.width, self.window.height))
            self.screen.blit(screen, (0, 0))

    def startGame(self, type):
        self.objectHandler.clearObjects()
        self.objectHandler.addObject(Player('00', int(self.window.width / 2), int(self.window.height / 2),
                                            60,
                                            80,
                                            type))
        self.objectHandler.addObject(Weapon('01', self.objectHandler.getObjectByID('00')))
        self.objectHandler.addObject(UIBar('03', self.objectHandler.getObjectByID('00'), UI.HEALTH, 50,
                                           self.window.height - 50,
                                           self.window.width / 6,
                                           self.window.height / 25))
        if self.objectHandler.getObjectByID('00').type == PlayerType.WIZARD:
            self.objectHandler.addObject(UIBar('04', self.objectHandler.getObjectByID('00'), UI.MAGIC,
                                           (self.window.width / 2) - ((self.window.width / 6) / 2),
                                           self.window.height - 50, self.window.width / 6,
                                           self.window.height / 25))
        elif self.objectHandler.getObjectByID('00').type == PlayerType.ROGUE:
            self.objectHandler.addObject(UIBar('04', self.objectHandler.getObjectByID('00'), UI.MAGIC,
                                            (self.window.width / 2) - ((self.window.width / 6) / 2),
                                            self.window.height - 50, self.window.width / 6,
                                            self.window.height / 25))
            self.objectHandler.addObject(UIBar('05', self.objectHandler.getObjectByID('00'), UI.STAMINA,
                                            (self.window.width - (self.window.width / 6) - 50),
                                            self.window.height - 50, self.window.width / 6,
                                            self.window.height / 25))
        self.state = GameState.GAME

    def loadMenu(self):
        background = pygame.image.load('./assets/MainMenu.png')
        background = pygame.transform.scale(background, (self.window.width, self.window.height))
        self.objectHandler.addObject(MainMenu('00', background, True))
        startGame = pygame.image.load('./assets/StartGame.png')
        startGame = pygame.transform.scale(startGame, (self.window.width, self.window.height))
        self.objectHandler.addObject(MainMenu('01', startGame, True))
        exit = pygame.image.load('./assets/Exit.png')
        exit = pygame.transform.scale(exit, (self.window.width, self.window.height))
        self.objectHandler.addObject(MainMenu('02', exit, False))

        startGameBack = pygame.image.load('./assets/StartGameBack.png')
        startGameBack = pygame.transform.scale(startGameBack, (self.window.width, self.window.height))
        self.objectHandler.addObject(MainMenu('03', startGameBack, False))
        wizardMenu = pygame.image.load('./assets/WizardMenu.png')
        wizardMenu = pygame.transform.scale(wizardMenu, (self.window.width, self.window.height))
        self.objectHandler.addObject(MainMenu('04', wizardMenu, False))
        knightMenu = pygame.image.load('./assets/KnightMenu.png')
        knightMenu = pygame.transform.scale(knightMenu, (self.window.width, self.window.height))
        self.objectHandler.addObject(MainMenu('05', knightMenu, False))
        rogueMenu = pygame.image.load('./assets/RogueMenu.png')
        rogueMenu = pygame.transform.scale(rogueMenu, (self.window.width, self.window.height))
        self.objectHandler.addObject(MainMenu('06', rogueMenu, False))
