from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]

for x in range(0,500,20):
    for y in range(0,500,20):
        draw_line(x,y, x**2 % 256,y**2 % 256,screen,random.sample(range(0,255),3))

display(screen)
save_extension(screen, 'img.png')