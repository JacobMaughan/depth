# Description: The weapon file for the python game Depth
# Created By: Jacob Maughan

# Imports
from Enums import PlayerType

import pygame

class Weapon:

    def __init__(self, ID, player):
        self.ID = ID
        self.player = player
        self.x = 0
        self.y = 0
        self.velX = 0
        self.velY = 0

        if player.type == PlayerType.WIZARD:
            self.width = 64
            self.height = 64
            self.xOff = -5
            self.yOff = -15
            self.sprite = pygame.image.load('./assets/player/Staff.png')
            self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        elif player.type == PlayerType.KNIGHT:
            self.width = 64
            self.height = 64
            self.xOff = -5
            self.yOff = -15
            self.sprite = pygame.image.load('./assets/player/Sword.png')
            self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        elif player.type == PlayerType.ROGUE:
            self.width = 32
            self.height = 32
            self.xOff = 0
            self.yOff = -10
            self.sprite = pygame.image.load('./assets/player/Dagger.png')
            self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))

    def tick(self, stateHandler):
        self.x = self.player.x + self.xOff
        self.y = self.player.y + self.yOff

    def render(self, screen):
        screen.blit(self.sprite, (self.x + 5, self.y))
