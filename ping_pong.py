from pygame import *


window = display.set_mode((700, 500))
window.fill((200, 255, 255))

class GameSprite(sprite.Sprite):
    #class constructor
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        # each sprite must store an image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # each sprite must store the rect property it is inscribed in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Racket(GameSprite):
    def move_r(self):
        keys = key.get_pressed()
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed
    def move_l(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed


racket_l = Racket('racket.png', 20, 100, 10, 20, 110)
racket_r = Racket('racket.png', 680, 100, 10, 20, 110)
ball = GameSprite('tenis_ball.png', 200, 300, 10, 50, 50)

game = True
clock = time.Clock()
FPS = 60

dx = 3
dy = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((200, 255, 255))

    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.y > 450 or ball.rect.y < 0:
        dy = dy * (-1)

    if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
        dx = dx * (-1)


    ball.reset()

    
    racket_l.reset()
    racket_l.move_l()


    racket_r.reset()
    racket_r.move_r()

    display.update()
    clock.tick(FPS)