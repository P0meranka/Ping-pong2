from pygame import *
from random import randint, choice

font.init()
clock = time.Clock()
FPS = 60

lost = 0
wins = 0

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Ping-Pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (180, 0, 0)

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
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed
    
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, hero_image, hero_x, hero_y, size_x, size_y, hero_speed):
        super().__init__(hero_image, hero_x, hero_y, size_x, size_y, hero_speed)
        self.speed_x = hero_speed * choice([-1, 1])
        self.speed_y = hero_speed * choice([-1, 1])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.y <= 0 or self.rect.y >= win_height - self.rect.height:
            self.speed_y *= -1

player1 = Player('rocket.jpg', 30, 170, 30, 140, 5)
player2 = Player('rocket2.jpg', win_width - 60, 170, 30, 140, 5)
ball = Ball('ball.jpg', win_width//2 - 15, win_height//2 - 15, 30, 30, 3)

font1 = font.Font(None, 50)
lose1_text = font1.render('PLAYER 1 LOSE!', True, RED)
lose2_text = font1.render('PLAYER 2 LOSE!', True, RED)

game = True
finish = False
winner = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if e.type == KEYDOWN:
            if e.key == K_r and finish:
                finish = False
                winner = 0

                ball.rect.x = win_width//2 - 15
                ball.rect.y = win_height//2 - 15

                ball.speed_x = 3 * choice([-1, 1])
                ball.speed_y = 3 * choice([-1, 1])

                player1.rect.y = 170
                player2.rect.y = 170

    if not finish:
        player1.update_left()
        player2.update_right()
        ball.update()

        if sprite.collide_rect(ball, player1):
            if ball.speed_x < 0:
                ball.speed_x = -ball.speed_x
                ball.speed_x *= 1.05
        if sprite.collide_rect(ball, player2):
            if ball.speed_x > 0:
                ball.speed_x = -ball.speed_x
                ball.speed_x *= 1.05

        if ball.rect.x < 0:
            finish = True
            winner = 2
        if ball.rect.x > win_width:
            finish = True
            winner = 1

    window.fill(BLACK)

    player1.reset()
    player2.reset()
    ball.reset()

    if finish:
        if winner == 1:
            window.blit(lose2_text, (win_width//2 - 100, win_height//2 - 50))
        else:
            window.blit(lose1_text, (win_width//2 - 100, win_height//2 - 50))
        
        restart_text = font1.render('Press R to restart', True, WHITE)
        window.blit(restart_text, (win_width//2 - 120, win_height//2 + 50))

    display.update()
    clock.tick(FPS)


    display.update()
    clock.tick(FPS)
