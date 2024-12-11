#
#
# import pygame
#
#
# #C
# COLOR_ORANGE = (255, 128, 0)
# COLOR_WHITE = (255, 255, 255)
# COLOR_YELLOW = (255, 255, 0)
# COLOR_BLUE = (0, 0, 255)
# COLOR_BLACK = (0, 0 , 0)
#
# #E
# ENTITY_DAMAGE = {
#     'ImageFP0': 0,
#     'ImageFP1': 0,
#     'ImageFP2': 0,
#     'ImageFP3': 0,
#     'ImageFP4': 0,
#     'ImageFP5': 0,
#     'ImageFP6': 0,
#     'ImageFP7': 0,
#     'ImageFP8': 0,
#     'ImageFP9': 0,
#     'ImageFP10': 0,
#     'Player1': 1,
#     'Player1Power': 25,
#     'Enemy1': 1,
#     'Enemy1Power': 20,
#     'Enemy2': 1,
#     'Enemy2Power': 15,
#
# }
#
# ENTITY_HEALTH = {
#     'ImageFP0': 999,
#     'ImageFP1': 999,
#     'ImageFP2': 999,
#     'ImageFP3': 999,
#     'ImageFP4': 999,
#     'ImageFP5': 999,
#     'ImageFP6': 999,
#     'ImageFP7': 999,
#     'ImageFP8': 999,
#     'ImageFP9': 999,
#     'ImageFP10': 999,
#     'Player1': 300,
#     'Player1Power': 1,
#     'Enemy1': 50,
#     'Enemy1Power': 1,
#     'Enemy2': 60,
#     'Enemy2Power': 1,
#
# }
#
# ENTITY_SCORE = {
#     'ImageFP0': 0,
#     'ImageFP1': 0,
#     'ImageFP2': 0,
#     'ImageFP3': 0,
#     'ImageFP4': 0,
#     'ImageFP5': 0,
#     'ImageFP6': 0,
#     'ImageFP7': 0,
#     'ImageFP8': 0,
#     'ImageFP9': 0,
#     'ImageFP10': 0,
#     'Player1': 0,
#     'Player1Power': 0,
#     'Enemy1': 100,
#     'Enemy1Power': 0,
#     'Enemy2': 125,
#     'Enemy2Power': 0,
#
# }
#
# ENTITY_SPEED = {
#     'ImageFP0': 0,
#     'ImageFP1': 0,
#     'ImageFP2': 1,
#     'ImageFP3': 2,
#     'ImageFP4': 3,
#     'ImageFP5': 4,
#     'ImageFP6': 5,
#     'ImageFP7': 5,
#     'ImageFP8': 5,
#     'ImageFP9': 5,
#     'ImageFP10': 5,
#     'Player1': 5,
#     'Player1Power': 3,
#     'Enemy1': 1,
#     'Enemy1Power': 4,
#     'Enemy2': 1,
#     'Enemy2Power': 2,
#
# }
#
# ENTITY_POWER_DELAY = {
#     'Player1': 20,
#     'Enemy1': 100,
#     'Enemy2': 200,
#
# }
#
# EVENT_ENEMY = pygame.USEREVENT + 1
#
# #M
# MENU_OPTION = ('NEW GAME',
#                'SCORE',
#                'QUIT GAME')
#
# #P
# PLAYER_KEY_POWER = {'Player1': pygame.K_RCTRL
#
# }
#
# #S
#
# SPAWN_TIME = 4000
#
# #W
# WIND_WIDTH = 800
# WIND_HEIGHT = 450


import pygame

# C
COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)

# Dano das entidades
ENTITY_DAMAGE = {
    'ImageFP0': 0,
    'ImageFP1': 0,
    'ImageFP2': 0,
    'ImageFP3': 0,
    'ImageFP4': 0,
    'ImageFP5': 0,
    'ImageFP6': 0,
    'ImageFP7': 0,
    'ImageFP8': 0,
    'ImageFP9': 0,
    'ImageFP10': 0,
    'Player1': 1,
    'Player1Power': 25,
    'Enemy1': 1,
    'Enemy1Power': 20,
    'Enemy2': 1,
    'Enemy2Power': 15,
}

# Saúde das entidades
ENTITY_HEALTH = {
    'ImageFP0': 999,
    'ImageFP1': 999,
    'ImageFP2': 999,
    'ImageFP3': 999,
    'ImageFP4': 999,
    'ImageFP5': 999,
    'ImageFP6': 999,
    'ImageFP7': 999,
    'ImageFP8': 999,
    'ImageFP9': 999,
    'ImageFP10': 999,
    'Player1': 300,
    'Player1Power': 1,
    'Enemy1': 50,
    'Enemy1Power': 1,
    'Enemy2': 60,
    'Enemy2Power': 1,
}

# Pontuação das entidades
ENTITY_SCORE = {
    'ImageFP0': 0,
    'ImageFP1': 0,
    'ImageFP2': 0,
    'ImageFP3': 0,
    'ImageFP4': 0,
    'ImageFP5': 0,
    'ImageFP6': 0,
    'ImageFP7': 0,
    'ImageFP8': 0,
    'ImageFP9': 0,
    'ImageFP10': 0,
    'Player1': 0,
    'Player1Power': 0,
    'Enemy1': 100,
    'Enemy1Power': 0,
    'Enemy2': 125,
    'Enemy2Power': 0,
}

# Velocidade das entidades
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
    'Player1Power': 3,
    'Enemy1': 1,
    'Enemy1Power': 4,
    'Enemy2': 1,
    'Enemy2Power': 2,
}

# Atraso para ativar poderes
ENTITY_POWER_DELAY = {
    'Player1': 20,
    'Enemy1': 100,
    'Enemy2': 200,
}

# Eventos personalizados
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# M
MENU_OPTION = ('NEW GAME', 'SCORE', 'QUIT GAME')

# Teclas associadas ao poder do jogador
PLAYER_KEY_POWER = {
    'Player1': pygame.K_RCTRL
}

# S
SPAWN_TIME = 4000

#T

TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

# Dimensões da janela
WIND_WIDTH = 800
WIND_HEIGHT = 450
