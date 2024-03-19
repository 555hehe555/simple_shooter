import pygame

pygame.init()

bullets = pygame.sprite.Group()


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, window, x=0, y=0, width=10, height=10, health=100):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(img), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.health = health
        self.window = window

    def create(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(GameSprite):
    ...


class Hero(GameSprite):
    def fire(self):
        bullet = Bullet("./img/window_icon128", self.rect.centerx, self.rect.centery, 20, 10, 1)
        bullets.add(bullet)


class Zombie(GameSprite):
    def run(self):
        self.rect.x += 10
