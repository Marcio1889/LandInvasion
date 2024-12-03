import pygame

#C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

#E

ENTITY_SPEED = {
    'ImageFP0': 0,
    'ImageFP1': 0,
    'ImageFP2': 1,
    'ImageFP3': 2,
    'ImageFP4': 3,
    'ImageFP5': 4,
    'ImageFP6': 5,
    'ImageFP7': 5,
    'ImageFP8': 5,
    'ImageFP9': 5,
    'ImageFP10': 5,
    'Player1': 5,
    'Enemy1': 2,
    'Enemy2': 1,

}

EVENT_ENEMY = pygame.USEREVENT + 1

#M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'QUIT GAME')

#S

SPAWN_TIME = 4000

#W
WIND_WIDTH = 800
WIND_HEIGHT = 450