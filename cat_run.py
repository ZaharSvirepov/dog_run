from pygame import *
from random import *
#? Классы 
#TODO Класс GameSprite 
class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, player_speed_y, ):
        #?вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #*каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.speed_y = player_speed_y

        #*каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #?метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#TODO Создаём класс игрока
class Player(GameSprite):
    #*метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_SPACE] and collider == True:
            self.speed_y = 16
            self.rect.y -= self.speed_y
        if collider == True:
            self.rect.y += 0     
        if collider == False:
            self.speed_y -= 1
            self.rect.y -= self.speed_y

#TODO Создаём класс платформ
class Platforms(GameSprite):
    #* Метод движения платформ
    def update(self):
        self.rect.x -= self.speed

        if self.rect.x < -50:
            self.rect.x = 1000
collider = True
coordinate = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050]
display.set_caption("cat_run")
window = display.set_mode((1000, 400))
background = transform.scale(image.load('trees.png'), (1000, 400))
platforms = sprite.Group()
cat_player = Player('cat.png', 200, 260, 80, 50, None, 16)
finish = False
for i in coordinate:
    platform = Platforms('platform.png', i, 320, 50, 80, 2, None)
    platforms.add(platform)
clock = time.Clock()
FPS = 60
run = True 
while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish == False:
        collider = False
        window.blit(background, (0, 0))
        cat_player.reset()
        platforms.draw(window)
        if sprite.spritecollide(cat_player, platforms, False):
            collider = True
        cat_player.update()
        platforms.update()
        clock.tick(FPS) 
        display.update() 

