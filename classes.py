import pygame
import random

pygame.init()

bullets = pygame.sprite.Group()

SCREEN_WIDTH, SCREEN_HEIGHT = 960, 540



class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, window, x=0, y=0, width=10, height=10, health=1, speed=10, direction="up", start_fire_coords=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(img).convert_alpha(), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.health = health
        self.window = window
        self.speed = speed
        self.direction = direction
        self.start_fire_coords = start_fire_coords

    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

    #
    # def collidepoint(self, x, y):
    #     return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Bullet(GameSprite):
    def current_hero_coords(self, hero_coords):
        self.start_fire_coords = hero_coords

    def cler_bullet(self):
        self.kill()

    def update(self):
        if self.rect.x >= 850 or self.rect.x <= 100 \
                or self.rect.y >= 440 or self.rect.y <= 100:
            self.kill()

        if self.direction == "right":
            if self.rect.x - self.start_fire_coords[0] > 165:
                self.rect.y += 0.5
            if self.rect.x - self.start_fire_coords[0] > 100:
                self.kill()
            self.rect.x += 4

        if self.direction == "left":
            if self.start_fire_coords[0] - self.rect.x > 165:
                self.rect.y += 0.5
            if self.start_fire_coords[0] - self.rect.x > 100:
                self.kill()
            self.rect.x -= 4

        if self.direction == "up":

            if self.start_fire_coords[1] - self.rect.y > 110:
                self.rect.x -= 1

            if self.start_fire_coords[1] - self.rect.y > 150:
                self.kill()
            self.rect.y -= 4

        if self.direction == "down":
            if self.rect.y - self.start_fire_coords[1] > 110:
                self.rect.x -= 1
            if self.rect.y - self.start_fire_coords[1] > 155:
                self.kill()
            self.rect.y += 4


class Hero(GameSprite):
    def show_coords(self):
        return [self.rect.centerx, self.rect.centery]

    def fire(self, window, direction):

        bullet = Bullet("./img/bullet.png", window, self.rect.centerx, self.rect.centery, 15, 15, 1, 12, direction)
        bullets.add(bullet)
        return bullets

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 70:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < SCREEN_WIDTH - self.width - 100:
            self.rect.x += self.speed

        if keys[pygame.K_w] and self.rect.y > 50:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < SCREEN_HEIGHT - self.height - 100:
            self.rect.y += self.speed


class Zombie(GameSprite):
    def update(self, hero_coord):
        if self.rect.x != hero_coord[0] or self.rect.y != hero_coord[1]:
            if self.rect.x >= hero_coord[0]:
                self.rect.x -= 1 - random.randint(-4, 3)
            if self.rect.x <= hero_coord[0]:
                self.rect.x += 1 - random.randint(-4, 3)

            if self.rect.y >= hero_coord[1]:
                self.rect.y -= 1 - random.randint(-4, 3)
            if self.rect.y <= hero_coord[1]:
                self.rect.y += 1 - random.randint(-4, 3)
