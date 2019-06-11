class Particle(object):
    def __init__(self, x_pos, y_pos, x_vel = 0, y_vel = 0):
        self.position = [x_pos, y_pos]
        self.velocity = [x_vel, y_vel]
        self.bounce_factor = 0.8

    def apply_acceleration(self, x, y):
        self.velocity[0] += x
        self.velocity[1] += y
    
    def update(self):
        for axis in range(0, 2):
            self.position[axis] += self.velocity[axis]
    
    def bounce(self, axis):
        self.velocity[axis] *= -self.bounce_factor
    
    def get_position(self):
        return (int(self.position[0]), int(self.position[1]))