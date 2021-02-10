# Description: This is the window file for the python game template
# Created By: Jacob Maughan

# Imports
import pygame

class Window:

    def __init__(self, width, height, title, img):
        self.width = width
        self.height = height
        self.title = title
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)
        pygame.display.set_icon(pygame.image.load(img))

    def fillScreen(self, r, g, b):
        self.screen.fill((r, g, b))
