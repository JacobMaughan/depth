# Description: The player class for the python game Depth
# Created By: Jacob Maughan

# Imports
from Enums import PlayerType
from Enums import GameState

import pygame

class Player:
    def __init__(self, ID, x, y, width, height, type):
        self.ID = ID
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
        self.velX = 0
        self.velY = 0
        self.maxStamina = 1000
        self.stamina = self.maxStamina
        self.money = 0

        if self.type == PlayerType.WIZARD:
            self.sprite = pygame.image.load('./assets/player/Wizard.png')
            self.sprite = pygame.transform.scale(self.sprite, (width, height))
            self.maxHealth = 100
            self.health = self.maxHealth
            self.maxMagic = 200
            self.magic = self.maxMagic
            self.speed = 1
            self.damage = 25
        elif self.type == PlayerType.KNIGHT:
            self.sprite = pygame.image.load('./assets/player/Knight.png')
            self.sprite = pygame.transform.scale(self.sprite, (width, height))
            self.maxHealth = 200
            self.health = self.maxHealth
            self.maxMagic = 0
            self.magic = self.maxHealth
            self.speed = 0.5
            self.damage = 50
        elif self.type == PlayerType.ROGUE:
            self.sprite = pygame.image.load('./assets/player/Rogue.png')
            self.sprite = pygame.transform.scale(self.sprite, (width, height))
            self.maxHealth = 50
            self.health = self.maxHealth
            self.maxMagic = 50
            self.magic = self.maxHealth
            self.speed = 1
            self.damage = 10

    def tick(self, stateHandler):
        self.x += self.velX * self.speed
        self.y += self.velY * self.speed
        self.getCollision(stateHandler)
        if self.type == PlayerType.ROGUE:
            if self.speed > 1:
                self.stamina -= 10
            if self.speed <= 1:
                self.stamina += 1
                if self.stamina > self.maxStamina:
                    self.stamina = self.maxStamina
            if self.stamina < 1:
                self.speed = 1
        if self.health <= 0:
            stateHandler.state = GameState.GAME_OVER

    def render(self, screen):
        screen.blit(self.sprite, (self.x - (self.width / 2), self.y - (self.height / 2)))

    def getCollision(self, stateHandler):
        if stateHandler.mapHandler.isChest:
            if self.x - self.width / 2 < 0:
                self.x = self.width / 2
            if self.y - self.height / 2 < 0:
                self.y = self.height / 2
            if self.x + self.width / 2 > stateHandler.window.width:
                self.x = stateHandler.window.width - self.width / 2
            if self.y + self.height / 2 > stateHandler.window.height:
                self.y = stateHandler.window.height - self.height / 2
