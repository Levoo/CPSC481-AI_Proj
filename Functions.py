import pygame
import sys

def check_keydown_events(event, main):
    if event.key == pygame.K_LEFT:
        main.px -= main.speed
    elif event.key == pygame.K_RIGHT:
        main.px += main.speed
    elif event.key == pygame.K_UP:
        main.py -= main.speed
    elif event.key == pygame.K_DOWN:
        main.py += main.speed


def check_events(play_button, main):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, mouse_x, mouse_y)
        elif event.type == pygame.MOUSEBUTTONUP:
            play_button.pressed = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            main.rect.x -= main.speed
        if keys[pygame.K_RIGHT]:
            main.rect.x += main.speed
        if keys[pygame.K_UP]:
            main.rect.y -= main.speed
        if keys[pygame.K_DOWN]:
            main.rect.y += main.speed


def check_play_button(play_button, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        play_button.pressed = True
    