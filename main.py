from classes import *
import sys
import pygame
import time
import random

pygame.init()
pygame.mixer.init()

window_icon = pygame.image.load("./img/isaac.png")

SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540
bg_color = (115, 81, 132)
pygame.display.set_caption("Binding of Isaac: Demo")
pygame.display.set_icon(window_icon)
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(bg_color)

bg_img = pygame.transform.scale(pygame.image.load("./img/bg.png").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_no_img = pygame.transform.scale(pygame.image.load("./img/bg_no_doors.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg = bg_img

bg_no_song = pygame.mixer.Sound("./sounds/bg_yes.wav")
bg_yes_song = pygame.mixer.Sound("./sounds/bg_no.mp3")
bg_song = None
shoot_song = pygame.mixer.Sound("./sounds/shoot.mp3")
hitting_song = pygame.mixer.Sound("./sounds/hitting.mp3")

hero_img = "./img/isaac.png"
zombie_img = "./img/muxu.png"

hero = Hero(hero_img, window, (SCREEN_WIDTH / 2) - 40, (SCREEN_HEIGHT / 2) - 50, 54, 64, health=3)

zombies = pygame.sprite.Group()
bullets = pygame.sprite.Group()


def zombie_create():
    for i in range(20):
        zombie = Zombie(zombie_img, window, random.randint(0, SCREEN_WIDTH - 100),
                        random.randint(100, SCREEN_HEIGHT - 100), 25, 20)
        zombies.add(zombie)


is_running = True
clock = pygame.time.Clock()
start_bullet_coords = []
current_hero_coords = 0

while is_running:
    window.blit(bg, (0, 0))
    hero.reset()
    hero.update()

    if current_hero_coords:
        for bullet in bullets:
            bullet.current_hero_coords(current_hero_coords)

    if bullets:
        for bullet in bullets:
            bullet.reset()
            bullet.update()

    if zombies:
        if bg_song is None:
            bg_song = bg_yes_song
        if bg_song == bg_no_song:
            bg_song.stop()
            bg_song = bg_yes_song
        if bg_song.get_num_channels() == 0:
            bg_song.play()

        zombies.update(hero.show_coords())

        zombies.draw(window)

        for z in zombies:
            if z.colliderect(hero.rect):
                print(hero.health)
                hero.health -= 0.5

        bg = bg_no_img

    if not zombies:
        if bg_song is None:
            bg_song = bg_no_song
        if bg_song == bg_yes_song:
            bg_song.stop()
            bg_song = bg_no_song
        if bg_song.get_num_channels() == 0:
            bg_song.play()

        bg = bg_img
        if hero.show_coords()[0] >= 800 and \
                200 <= hero.show_coords()[1] <= 250:
            hero.rect.x = 100
            zombie_create()
            for b in bullets:
                b.cler_bullet()
        elif hero.show_coords()[0] <= 100 and \
                200 <= hero.show_coords()[1] <= 250:
            hero.rect.x = 810
            zombie_create()
            for b in bullets:
                b.cler_bullet()

        elif hero.show_coords()[1] <= 100 and \
                400 <= hero.show_coords()[0] <= 500:
            hero.rect.y = 380
            zombie_create()
            for b in bullets:
                b.cler_bullet()
        elif hero.show_coords()[1] >= 380 and \
                400 <= hero.show_coords()[0] <= 500:
            hero.rect.y = 50
            zombie_create()
            for b in bullets:
                b.cler_bullet()

    if zombies and bullets:
        collides = pygame.sprite.groupcollide(zombies, bullets, True, True)
        if collides:
            hitting_song.play()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and len(bullets) < 5:
            if event.key == pygame.K_RIGHT:
                bullets = hero.fire(window, "right")
                current_hero_coords = hero.show_coords()
                shoot_song.play()

            if event.key == pygame.K_LEFT:
                bullets = hero.fire(window, "left")
                current_hero_coords = hero.show_coords()
                shoot_song.play()

            if event.key == pygame.K_UP:
                bullets = hero.fire(window, "up")
                current_hero_coords = hero.show_coords()
                shoot_song.play()

            if event.key == pygame.K_DOWN:
                bullets = hero.fire(window, "down")
                current_hero_coords = hero.show_coords()
                shoot_song.play()

    clock.tick(60)
