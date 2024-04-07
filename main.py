from classes import *
import sys
import pygame
import time
import random

pygame.init()

window_icon = pygame.image.load("./img/isaac.png")

SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
bg_color = (115, 81, 132)
pygame.display.set_caption("Binding of Isaac: Repentance")
pygame.display.set_icon(window_icon)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(bg_color)

bg_img = pygame.transform.scale(pygame.image.load("./img/bg.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

hero_img = "./img/isaac.png"
zombie_img = "./img/muxu.png"

hero = Hero(hero_img, window, (SCREEN_WIDTH / 2) - 40, (SCREEN_HEIGHT / 2) - 50, 54, 64)

zombies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

for i in range(10):
    zombie = Zombie(zombie_img, window, random.randint(0, SCREEN_WIDTH - 100),
                    random.randint(0, SCREEN_HEIGHT - 100), 25, 20)
    zombies.add(zombie)

is_running = True
clock = pygame.time.Clock()
start_bullet_coords = []

while is_running:

    print(clock.get_fps())
    window.blit(bg_img, (0, 0))
    hero.reset()
    hero.update()

    # bullets = hero.fire(window)
    print(len(bullets))

    for bullet in bullets:
        bullet.reset()
        bullet.update()

    zombies.update(hero.show_coords())

    zombies.draw(window)

    for z in zombies:
        a = z.colliderect(hero.rect)
        if a:
            print("dfggg")

    collides = pygame.sprite.groupcollide(zombies, bullets, True, True)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and len(bullets) < 5:
            if event.key == pygame.K_RIGHT:
                bullets = hero.fire(window, "right")
                hero_cordc = hero.show_coords()
                start_bullet_coords.append(hero_cordc)

            if event.key == pygame.K_LEFT:
                bullets = hero.fire(window, "left")
                hero_cordc = hero.show_coords()
                start_bullet_coords.append(hero_cordc)

            if event.key == pygame.K_UP:
                bullets = hero.fire(window, "up")
                hero_cordc = hero.show_coords()
                start_bullet_coords.append(hero_cordc)

            if event.key == pygame.K_DOWN:
                bullets = hero.fire(window, "down")
                hero_cordc = hero.show_coords()
                start_bullet_coords.append(hero_cordc)


    clock.tick(60)
