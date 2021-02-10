# Description: The main file for the python game template
# Created By: Jacob Maughan

# Imports
from Window import Window
from GameStateHandler import GameStateHandler

import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = Window(1280, 760, 'Depth', './assets/player/Wizard.png')
        self.running = None
        self.gameStateHandler = GameStateHandler(self.window, self)

    def tick(self):
        self.gameStateHandler.tick()

    def render(self):
        self.window.fillScreen(0, 0, 0)
        self.gameStateHandler.render()
        pygame.display.update()

    def start(self):
        self.running = True
        self.loop()

    def stop(self):
        self.running = False

    def loop(self):
        while self.running:
            self.tick()
            self.render()

game = Game()
game.start()
