import pymunk
import pygame
import pymunk.pygame_util
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))
draw_options = pymunk.pygame_util.DrawOptions(screen)
space = pymunk.Space()
space.gravity = 0, -100
body = pymunk.Body (1, 20) # Body(mass, moment, body_type
body.position = 50,550 # body_type : DYNAMIC, KINEMATIC, STATIC
shape = pymunk.Circle (body, 10, (0,0)) # Circle(body, r,
space.add(body, shape) # objs

clock = pygame.time.Clock()

for i in range(0, 500):
    screen.fill((255, 255, 255, 255))
    space.debug_draw(draw_options)
    space.step((1/50.0))
    pygame.display.flip()
    clock.tick(50)

pygame.quit()