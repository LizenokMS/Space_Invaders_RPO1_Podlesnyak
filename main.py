import pygame
import sys
import controls
from hero import Hero
from pygame.sprite import Group

def start_game():
    '''основная функция для описания игры'''
    pygame.init()
    screen = pygame.display.set_mode((600, 900))
    pygame.display.set_caption("Space Invaders")

    #объекты классов
    hero = Hero(screen)
    bullets = Group()
    enemys = Group()

    flag = True
    while flag:

        controls.events(hero, screen, bullets)

        # screen.fill(0)
        hero.moving_hero(screen)
        controls.update(screen, hero, bullets)
        controls.create_army(screen)
        