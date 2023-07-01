import pygame as pg
import random
pg.init()
win_width, win_height = 800, 600 
window = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("Шутер")
class GameSprite:
    def __init__(self, image, x, y, width, height, speed):
        self.width = width
        self.height = height
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load(image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def control1(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_s] and self.rect.y < 600-250:
            self.rect.y += self.speed
        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
    def control2(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_DOWN] and self.rect.y < 600-250:
            self.rect.y += self.speed
        if keys[pg.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
class Ball(GameSprite):
    def move(self):
        global x2, y2, player1, player2, score1, score2
        self.rect.x += x2
        self.rect.y += y2
        if pg.sprite.collide_rect(player2, self):
            x2 = -5
        if pg.sprite.collide_rect(player1, self):
            x2 = 5
        if self.rect.y < 0:
            y2 = 5
        if self.rect.y > 525:
            y2 = -5
        if self.rect.x < 0:
            score2 += 1
            self.rect.x = 400  
        if self.rect.x > win_width - self.width:
            score1 += 1
            self.rect.x = 400  
x2, y2 = 9, 5  

def check_score():
    global score1, score2
    if score1 >= 5 or score2 >= 5:
        return True
    return False

def game_over():
    global score1, score2
    if score1 >= 5:
        print("Игрок 1 победил!")
    elif score2 >= 5:
        print("Игрок 2 победил!")
         
x2, y2 = 9, 5
score1, score2 = 0, 0




back =GameSprite("image/fon.png",0,0,800,600,0)
player1 = Player("image/c1.png",0,300,20,200,5)
player2 = Player("image/c2.png",780,300,20,200,5)
ball = Ball("image/ball.png", 450, 275, 25, 25, 1)
game = True
while game:
    if score1 >= 10:
        game_over = "image/win1.png"
        Game = False
    if score2 >= 10:
        game_over = "image/win2.png"
        Game = False
    back.reset()
    pg.time.Clock().tick(144)
    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
    if score1 >=5:
        game_over = "image/win1.png"
    if score2 >=5:
        game_over = "image/win2.png" 
    back.reset()
    player1.reset()
    player1.control1()
    player2.reset()
    player2.control2()
    ball.reset()
    ball.move()
    label1 = pg.font.SysFont('MS Sans Serif', 25).render(f"win: {score1}", True, "white")
    window.blit(label1,(20,20))
    label1 = pg.font.SysFont('MS Sans Serif', 25).render(f"win: {score2}", True, "white")
    window.blit(label1,(730,20))
    pg.display.flip()