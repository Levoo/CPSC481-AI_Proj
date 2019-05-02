import pygame
import sys


def check_events(play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse):
                play_button.press = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse):
                play_button.pressed = True
            else:
                play_button.press = False
