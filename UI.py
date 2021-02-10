# Description: The UI file for the python game Depth
# Created By: Jacob Maughan

# Imports
from Enums import UI

import pygame

class UIBar:

    def __init__(self, ID, player, type, x, y, width, height):
        self.ID = ID
        self.player = player
        self.type = type
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.length = 0

    def tick(self, stateHandler):
        if self.type == UI.HEALTH:
            self.length = self.player.health / self.player.maxHealth
        elif self.type == UI.MAGIC:
            self.length = self.player.magic / self.player.maxMagic
        elif self.type == UI.STAMINA:
            self.length = self.player.stamina / self.player.maxStamina

    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (128, 128, 128), (self.x + 5, self.y + 5, self.width - 10, self.height - 10))
        if self.type == UI.HEALTH:
            pygame.draw.rect(screen, (255, 0, 0), (self.x + 5, self.y + 5, (self.width - 10) * self.length, self.height - 10))
        elif self.type == UI.STAMINA:
            pygame.draw.rect(screen, (0, 255, 0), (self.x + 5, self.y + 5, (self.width - 10) * self.length, self.height - 10))
        elif self.type == UI.MAGIC:
            pygame.draw.rect(screen, (0, 0, 255), (self.x + 5, self.y + 5, (self.width - 10) * self.length, self.height - 10))
