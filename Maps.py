# Description: This file hold all of the maps for the python game Depth
# Created By: Jacob Maughan

# Import
import random

maps01 = [
    "WWWWWWWWW..WWWWWWWWW",
    "i..................i",
    "....................",
    "....................",
    "....................",
    "....................",
    "....................",
    "....................",
    "....................",
    "i..................i",
    "BBBBBBBBB..BBBBBBBBB"
]

maps02 = [
    "WWWWWWWWW..WWWWWWWWW",
    "C..................i",
    "....................",
    "....................",
    "....................",
    "....................",
    "....................",
    "....................",
    "....................",
    "i..................i",
    "BBBBBBBBB..BBBBBBBBB"
]

maps03 = [
    "WWWWWWWWW..WWWWWWWWW",
    "S..................i",
    "....................",
    "....................",
    "....................",
    "....................",
    "....................",
    "....................",
    "....................",
    "i..................i",
    "BBBBBBBBB..BBBBBBBBB"
]

def randMap():
    r = random.randint(1, 3)
    if r == 1:
        return maps01
    elif r == 2:
        return maps02
    elif r == 3:
        return maps03

def getMap(map):
    if map == 1:
        return maps01
    elif map == 2:
        return maps02
    elif map == 3:
        return maps03
