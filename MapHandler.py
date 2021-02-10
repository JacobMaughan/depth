# Description: The map handler for the python game Depth
# Created By: Jacob Maughan

# Imports
import Maps

import pygame


class MapHandler:

    def __init__(self, window):
        self.screen = window.screen
        self.width = window.width
        self.height = window.height
        self.map = Maps.getMap(2)
        self.isChest = False
        self.loadSprites()

    def render(self):
        chestCheck = False
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                if self.map[y][x] == '.':
                    self.screen.blit(self.floor, (x * self.width / 20, y * self.height / 11))
                elif self.map[y][x] == 'W':
                    self.screen.blit(self.wall, (x * self.width / 20, y * self.height / 11))
                elif self.map[y][x] == 'B':
                    self.screen.blit(self.void, (x * self.width / 20, y * self.height / 11))
                    self.screen.blit(self.bottom, (x * self.width / 20, y * self.height / 11))
                elif self.map[y][x] == 'C':
                    chestCheck = True
                    self.screen.blit(self.chest, (x * self.width / 20, y * self.height / 11))
                elif self.map[y][x] == 'i':
                    self.screen.blit(self.floor, (x * self.width / 20, y * self.height / 11))
                    self.screen.blit(self.torch, (x * self.width / 20 + self.width / 40, y * self.height / 11))
        if chestCheck:
            self.isChest = True
        else:
            self.isChest = False

    def loadSprites(self):
        self.floor = pygame.image.load('./assets/environment/Floor.png')
        self.floor = pygame.transform.scale(self.floor, (int(self.width / 20), int(self.height / 11)))
        self.wall = pygame.image.load('./assets/environment/Wall.png')
        self.wall = pygame.transform.scale(self.wall, (int(self.width / 20), int(self.height / 11)))
        self.bottom = pygame.image.load('./assets/environment/Bottom.png')
        self.bottom = pygame.transform.scale(self.bottom, (int(self.width / 20), int(self.height / 11)))
        self.void = pygame.image.load('./assets/environment/Void.png')
        self.void = pygame.transform.scale(self.void, (int(self.width / 20), int(self.height / 11)))
        self.chest = pygame.image.load('./assets/environment/Chest.png')
        self.chest = pygame.transform.scale(self.chest, (int(self.width / 20), int(self.height / 11)))
        self.torch = pygame.image.load('./assets/environment/Torch.png')
        self.torch = pygame.transform.scale(self.torch, (16, 50))
