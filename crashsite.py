# -*- coding: utf-8 -*-
import sys
import os

if sys.platform == "darwin":  # If the user's OS = MacOS...
    # Installs files necessary for the 'PyGame' library.
    os.system('pip3 install --user pygame')
    print("* Finished library install *")

if sys.platform == "win32":  # If the user's OS = Windows...
    os.system('pip install --user pygame')
    print("* Finished library install *")

import pygame
print("* Using PyGame version", pygame.__version__.__str__(), "*")

x = 20
y = 20
width = 20
height = 20
vel = 5


def setup():
    # Create screen
    pygame.init()  # This line causes an APIS warning on MacOS. Check "Issues"
    screen = pygame.display.set_mode((1280, 800))
    pygame.display.set_caption('Shitty Blackjack')

    # Set background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((150, 0, 50))

    # Blit to screen (render)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    eventLoop(screen, background)


def eventLoop(screen, background):
    global width, height, x, y, vel
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 1280-width-vel:
            x += vel
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 800-height-vel:
            y += vel

        screen.fill((150, 0, 50))
        pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
        pygame.display.update()


def main():
    setup()


main()  # Last line of code, runs main code.
