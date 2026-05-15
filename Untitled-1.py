from pygame import *

font.init()

lost = 0
wins = 0

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')

class GameSprite(sprite.Sprite):
    def __init__(self, hero_image, hero_x, hero_y, size_x, size_y, hero_speed):
        super().__init__()
        self.image = transform.scale(image.load(hero_image), (size_x, size_y))
        self.speed = hero_speed
        self.rect = self.image.get_rect()
        self.rect.x = hero_x
        self.rect.y = hero_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
            self.rect.x += self.speed
        if keys(K_UP) and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys(K_DOWN) and self.rect.y < 400:
            self.rect.y += self.speed

player1 = ('Без имени.png', 30, 200, 20, 100, 5) 