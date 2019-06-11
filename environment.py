import pygame as pg

class Environment(object):
    def __init__(self, width, height, surface):
        self.acceleration = (0, 0)
        self.friction_coeficient = 1
        self.width, self.height = width, height
        self.particles = []
        self.surface = surface

    def set_acceleration(self, a):
        self.acceleration = a

    def add_particle(self, particle):
        self.particles.append(particle)

    def update_particles(self):
        for particle in self.particles:
            particle.apply_acceleration(*self.acceleration)
            
            if particle.position[0] + particle.velocity[0] <= 0 or particle.position[0] + particle.velocity[0] >= self.width:
                particle.bounce(0)
            if particle.position[1] + particle.velocity[1] <= 0 or particle.position[1] + particle.velocity[1] >= self.height:
                particle.bounce(1)
            particle.update()
    
    def draw_particles(self):
        for particle in self.particles:
            pg.draw.circle(self.surface, (255,0,0), particle.get_position(), 3)