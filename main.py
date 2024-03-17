import sys
import pygame
import time
import random

pygame.init()

window_icon = pygame.image.load("./img/window_icon512.png")

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 1024
bg_color = (115, 81, 132)
pygame.display.set_caption("Simple shooter!!!")
pygame.display.set_icon(window_icon)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# window.fill(bg_color)

is_running = True
pygame.display.update()
while is_running:



    time.sleep(0.05)
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    window.fill(bg_color)
    pygame.display.update()
    time.sleep(0.05)
    bg_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    window.fill(bg_color)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
            
pygame.quit()
sys.exit()