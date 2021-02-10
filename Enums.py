# Description: The enums file for the python game Depth
# Created By: Jacob Maughan

from enum import Enum

class PlayerType(Enum):
    WIZARD = 1
    KNIGHT = 2
    ROGUE = 3

class GameState(Enum):
    MAIN_MENU = 1
    GAME = 2
    GAME_SHOP = 3
    GAME_OVER = 4

class UI(Enum):
    HEALTH = 1
    MAGIC = 2
    STAMINA = 3
