import colorsys
import math

import pygame as pygame
from pygame import DOUBLEBUF, Vector2

from Sounds import Sounds

width = 1280
height = 720

screen = pygame.display.set_mode((width, height), DOUBLEBUF, 16)
clock = pygame.time.Clock()


def hueToRGB( hue):
    # Convert HSV to RGB
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
    # Scale RGB values to 0-255 range
    return (int(r * 255), int(g * 255), int(b * 255))


class Ball:
    def __init__(self,i, pos, gravity, hue, radius=10):
        self.i = i
        self.color = hueToRGB(hue)
        self.radius = radius
        self.pos = pos
        self.gravity = gravity

    def update(self, time):
        self.pos.y = (height - 100) + abs(math.sin(time/5 * self.gravity)) * -400

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)


time = 0
balls = []
totalBalls = 50
barY = height-95

x = 20
xStep = (width-20)/totalBalls
gravity = 1
hue = 0

for i in range(totalBalls):
    ball = Ball(i,Vector2(x, height-100),gravity *0.5,hue)
    x += xStep
    gravity += 1
    hue += 1/totalBalls
    balls.append(ball)


sound = Sounds()

while True:
    screen.fill((23, 23, 23), (0, 0, width, height))
    deltaTime = clock.tick(60)/1000
    time += deltaTime

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    for ball in balls:
        ball.update(time)
        if ball.pos.y + ball.radius > barY:
            sound.play_at(ball.i)

        ball.draw()
    for i in range(0, totalBalls - 1):
        pygame.draw.line(screen, (233, 233, 233), (balls[i].pos), (balls[i + 1].pos))

    pygame.draw.rect(screen, (233, 233, 233), (0, barY, width, 5))

    pygame.display.flip()
