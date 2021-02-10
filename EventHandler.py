# Description: This is the event handler for the python game template
# Created By: Jacob Maughan

# Imports
from Enums import PlayerType
from Enums import GameState

import pygame

class EventHandler:

    def __init__(self, game):
        self.game = game

    def tick(self, stateHandler):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.stop()

            objectHandler = stateHandler.objectHandler
            player = objectHandler.getObjectByID('00')

            if stateHandler.state == GameState.MAIN_MENU:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if objectHandler.getObjectByID('01').selected:
                            objectHandler.getObjectByID('01').selected = False
                            objectHandler.getObjectByID('02').selected = True
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        if objectHandler.getObjectByID('02').selected:
                            objectHandler.getObjectByID('02').selected = False
                            objectHandler.getObjectByID('01').selected = True
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        if objectHandler.getObjectByID('05').selected:
                            objectHandler.getObjectByID('05').selected = False
                            objectHandler.getObjectByID('04').selected = True
                        elif objectHandler.getObjectByID('06').selected:
                            objectHandler.getObjectByID('06').selected = False
                            objectHandler.getObjectByID('05').selected = True
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        if objectHandler.getObjectByID('04').selected:
                            objectHandler.getObjectByID('04').selected = False
                            objectHandler.getObjectByID('05').selected = True
                        elif objectHandler.getObjectByID('05').selected:
                            objectHandler.getObjectByID('05').selected = False
                            objectHandler.getObjectByID('06').selected = True
                    elif event.key == pygame.K_RETURN:
                        if objectHandler.getObjectByID('01').selected:
                            objectHandler.getObjectByID('00').selected = False
                            objectHandler.getObjectByID('01').selected = False
                            objectHandler.getObjectByID('02').selected = False
                            objectHandler.getObjectByID('03').selected = True
                            objectHandler.getObjectByID('05').selected = True
                        elif objectHandler.getObjectByID("02").selected:
                            self.game.stop()
                        elif objectHandler.getObjectByID('04').selected:
                            stateHandler.startGame(PlayerType.WIZARD)
                        elif objectHandler.getObjectByID('05').selected:
                            stateHandler.startGame(PlayerType.KNIGHT)
                        elif objectHandler.getObjectByID('06').selected:
                            stateHandler.startGame(PlayerType.ROGUE)

            elif stateHandler.state == GameState.GAME:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player.velY = -1
                    if event.key == pygame.K_a:
                        player.velX = -1
                    if event.key == pygame.K_s:
                        player.velY = 1
                    if event.key == pygame.K_d:
                        player.velX = 1
                    if event.key == pygame.K_LSHIFT and player.type == PlayerType.ROGUE:
                        player.speed = 4
                    if event.key == pygame.K_h:
                        player.health -= 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        player.velY = 0
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        player.velX = 0
                    if event.key == pygame.K_LSHIFT and player.type == PlayerType.ROGUE:
                        player.speed = 1

            elif stateHandler.state == GameState.GAME_SHOP:
                if event.type == pygame.KEYDOWN:
                    if event.ket == pygame.K_ESCAPE:
                        stateHandler.state = GameState.GAME

            elif stateHandler.state == GameState.GAME_OVER:
                if event.type == pygame.KEYDOWN:
                    objectHandler.clearObjects()
                    stateHandler.loadMenu()
                    stateHandler.state = GameState.MAIN_MENU
