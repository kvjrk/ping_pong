from pygame import *

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    key_pressed = key.get_pressed()
    def update_l(self):
        keys = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 630:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 630:
            self.rect.y += self.speed

racket1 = Player('racket.png', 30, win_height-100, 8, 100, 150)
racket1 = Player('racket.png', 520, win_height-100, 8, 100, 150)
ball = Player('tenis_ball', 200, 200, 4, 50,50)

game = True
finish = False 
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180,0,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        racket1.update_l()
        racket1.reset()
        racket2.update_r()
        racket2.reset()
        ball.update()
        ball.draw(window)

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
        
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket1, ball):
            speed_x *= -1
    display.update()
    clock.tick(FPS)

