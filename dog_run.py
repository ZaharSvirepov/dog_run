from pygame import *

display.set_caption("dog_run")
window = display.set_mode((1000, 400))
background = transform.scale(image.load('trees.png'), (1000, 400))

run = True 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    window.blit(background, (0 ,0))

    display.update()