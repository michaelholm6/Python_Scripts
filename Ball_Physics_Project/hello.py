
import pygame
import random
import math
(width, height) = (300, 200)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
number_of_particles = 10
my_particles = []

class Particle:
    def __init__(self, position, size):
        self.x, self.y = position
        self.size = size
        self.color = (0,0,255)
        self.thickness = 1
        self.speed = .01
        self.angle = 0

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size, self.thickness)

    def move(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

background_colour = (255,255,255)
screen.fill(background_colour)

for n in range(number_of_particles):
    size = random.randint(10,20)
    x = random.randint(size, width-size)
    y = random.randint(size, height - size)

    particle = Particle((x,y), size)
    particle.speed = random.random()
    particle.speed /= 100
    particle.angle = random.uniform(0, math.pi * 2)

    my_particles.append(particle)

running = True
while running:
    for particle in my_particles:
        particle.move()
        particle.display()

    pygame.display.flip()
    screen.fill(background_colour)

    for event in pygame.event.get():
        # pylint: disable=no-member, # this error doesn't matter, and it's annoying
        if event.type == pygame.QUIT:
            running = False



