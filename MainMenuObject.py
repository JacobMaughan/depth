# Description: The main menu object for the python game Depth
# Created By: Jacob Maughan

class MainMenu:

    def __init__(self, ID, img, selected):
        self.ID = ID
        self.img = img
        self.selected = selected

    def render(self, screen):
        if self.selected:
            screen.blit(self.img, (0, 0))
