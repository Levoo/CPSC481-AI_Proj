import pygame
import sys


def check_events(play_button, quit_button, increase_button, decrease_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or quit_button.pressed:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse):
                play_button.press = True
            elif quit_button.rect.collidepoint(mouse):
                quit_button.press = True
            elif increase_button.rect.collidepoint(mouse):
                increase_button.press = True
            elif decrease_button.rect.collidepoint(mouse):
                decrease_button.press = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse) and play_button.press is True:
                play_button.pressed = True
            elif quit_button.rect.collidepoint(mouse) and quit_button.press is True:
                quit_button.pressed = True
            elif increase_button.rect.collidepoint(mouse) and increase_button.press is True:
                increase_button.pressed = True
            elif decrease_button.rect.collidepoint(mouse) and decrease_button.press is True:
                decrease_button.pressed = True
            play_button.press = False
            quit_button.press = False
            increase_button.press = False
            decrease_button.press = False
