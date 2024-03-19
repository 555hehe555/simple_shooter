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

is_running = True

zombies = list()

for i in range(random.randint(5, 10)):
    zombie = Zombie(zombie_img, window, random.randint(0, 800), 300, 50, 70)
    print(zombie, zombies)
    zombies.append(zombie)
    print(zombie, zombies)

while is_running:
    # window.blit(window_icon,(0,0))
    hero.create()

    for item in zombies:
        item.create()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
