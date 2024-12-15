
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

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Music.Score.mp3')  # Definindo a música do menu
        pygame.mixer_music.play(-1)  # Deixando a música tocar infinitamente
        db = DB('scores.db')
        name = ''
        score = player_score[0] if game_mode == MENU_OPTION[0] else 0
        text = 'Player 1 enter your name (4 characters):'

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'You finished the level!', COLOR_ORANGE, SCORE_POS['Title'])
            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        db.close()
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(30, name, COLOR_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show(self):
        pygame.mixer_music.load('./asset/Music.Score.mp3')  # Definindo a música do menu
        pygame.mixer_music.play(-1)  # Deixando a música tocar infinitamente
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(58, 'TOP SCORE', COLOR_YELLOW, SCORE_POS['Title2'])
        self.score_text(30, 'NAME        SCORE         DATE', COLOR_ORANGE, SCORE_POS['Label'])

        db = DB('scores.db')
        list_score = db.retrieve_top()
        db.close()

        for i, player_score in enumerate(list_score):
            id_, name, score, date = player_score

            # Espaçamento ajustado
            formatted_name = f'{name:<9}'  # Nome com até 15 caracteres, alinhado à esquerda
            formatted_score = f'{score:>7}'  # Pontuação com 7 caracteres, alinhada à direita
            formatted_date = f'{date}'  # Data permanece inalterada

            # Y-offset dinâmico para alinhar linhas
            y_offset = SCORE_POS['Label'][1] + 40 + (i * 30)
            self.score_text(
                30,
                f'{formatted_name}{formatted_score}     {formatted_date}',  # Espaço entre colunas ajustado
                COLOR_WHITE,
                (SCORE_POS['Label'][0], y_offset)
            )

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    return
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="DejaVu Sans Mono", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
