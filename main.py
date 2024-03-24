from classes import *
import sys
import pygame
import time
import random

pygame.init()

window_icon = pygame.image.load("./img/window_icon512.png")

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
bg_color = (115, 81, 132)
pygame.display.set_caption("Simple shooter!!!")
pygame.display.set_icon(window_icon)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(bg_color)

bg_img = pygame.transform.scale(pygame.image.load("./img/img.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

hero_img = "./img/window_icon128.png"
zombie_img = "./img/windows_icon64.png"

hero = Hero(hero_img, window, (SCREEN_WIDTH/2)-40, (SCREEN_HEIGHT/2)-50, 100, 100)

zombies = pygame.sprite.Group()

for i in range(1000):
    zombie = Zombie("./img/img_1.png", window, random.randint(0, SCREEN_WIDTH-100),
                    random.randint(0, SCREEN_HEIGHT-100), 100, 100)
    zombies.add(zombie)

is_running = True
clock = pygame.time.Clock()
while is_running:
    print(clock.get_fps())
    window.blit(bg_img, (0, 0))
    hero.reset()
    hero.update()

    zombies.update(hero.show_coords())

    zombies.draw(window)

    for z in zombies:
        a = z.colliderect(hero.rect)
        if a:
            print("dfggg")

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()

    clock.tick(60)