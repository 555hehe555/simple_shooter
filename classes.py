import pygame

pygame.init()

bullets = pygame.sprite.Group()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, window, x=0, y=0, width=10, height=10, health=100, speed=10):
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

    def reset(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))

    #
    # def collidepoint(self, x, y):
    #     return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Bullet(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            self.rect.x += 1

        if keys[pygame.K_UP]:
            self.rect.y -= 1
        if keys[pygame.K_DOWN]:
            self.rect.y += 1


class Hero(GameSprite):
    def show_coords(self):
        return [self.rect.x, self.rect.y]

    def fire(self, window):
        bullet = Bullet("./img/muxu.png", window, self.rect.x, self.rect.y, 20, 10, 1)
        bullets.add(bullet)
        return bullets

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and self.rect.x < SCREEN_WIDTH - self.width:
            self.rect.x += self.speed

        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < SCREEN_HEIGHT - self.height:
            self.rect.y += self.speed


class Zombie(GameSprite):
    def update(self, hero_coord):
        if self.rect.x != hero_coord[0] or self.rect.y != hero_coord[1]:
            if self.rect.x > hero_coord[0]:
                self.rect.x -= 1
            elif self.rect.x < hero_coord[0]:
                self.rect.x += 1

            if self.rect.y > hero_coord[1]:
                self.rect.y -= 1
            elif self.rect.y < hero_coord[1]:
                self.rect.y += 1
