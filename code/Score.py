import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.DB import DB
from code.const import COLOR_ORANGE, SCORE_POS, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Image.Score.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass


    def save(self, game_mode:str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Music.Score.mp3')  # Definindo a música do menu
        pygame.mixer_music.play(-1)  # Deixando a música tocar infinitamente
        db = DB('scores.db')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(58, 'YOU WIN!', COLOR_ORANGE, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Player 1 enter you name (4 characters):'
            self.score_text(30, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                             name += event.unicode

            self.score_text(30, name, COLOR_WHITE, SCORE_POS['Name'])

            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Music.Score.mp3')  # Definindo a música do menu
        pygame.mixer_music.play(-1)  # Deixando a música tocar infinitamente
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(58, 'TOP 05 SCORE', COLOR_YELLOW, SCORE_POS['Title2'])
        self.score_text(30, 'NAME        SCORE             DATE     ', COLOR_WHITE, SCORE_POS['Label'])
        db = DB('scores.db')
        list_score = db.retrieve_top()
        db.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(30, f'{name}       {score: 05d}       {date}', COLOR_WHITE,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Arial", size=text_size)  # Fonte alterada para Arial
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"

