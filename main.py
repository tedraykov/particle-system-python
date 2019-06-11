import pygame as pg
import random

from particle import Particle
from environment import Environment
size = width, height = 800, 600
black = 0, 0, 0

def generate_particles(amount, environment):
    for i in range(0, amount):
        x = random.randrange(0, 800)
        y = random.randrange(0, 600)
        v_x, v_y = random.randrange(0,20), random.randrange(0,20)
        particle = Particle(x, y, v_x, v_y)
        environment.add_particle(particle)

screen = pg.display.set_mode(size)
clock = pg.time.Clock()
environment = Environment(*size, screen)

environment.set_acceleration((0, 0.8))
generate_particles(20, environment)

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            run = False

    screen.fill(black)

    environment.update_particles()
    environment.draw_particles()
    
    pg.display.update()
    clock.tick(30)
pg.quit()