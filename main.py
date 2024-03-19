from classes import *
import sys
import pygame
import time
import random

pygame.init()

window_icon = pygame.image.load("./img/window_icon512.png")
hero_img = "./img/window_icon128.png"
zombie_img = "./img/windows_icon64.png"

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
bg_color = (115, 81, 132)
pygame.display.set_caption("Simple shooter!!!")
pygame.display.set_icon(window_icon)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(bg_color)

hero = GameSprite(hero_img, window, 400, 300, 100, 100)

zombies = pygame.sprite.Group()

for i in range(1, 6):
    zombie = Zombie("./img/windows_icon64.png", window, 300, 400, 100, 100)
    zombies.add(zombie)

is_running = True

while is_running:
    # window.blit(window_icon,(0,0))
    hero.create()

    zombies.update()
    zombies.draw(window)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()