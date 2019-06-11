# -*- coding: utf-8 -*-
""" UN-COMMENT THIS CODE BEFORE RUNNING IT ON A COMPUTER FOR THE FIRST TIME!
import sys
import os

if sys.platform == "darwin":  # If the user's OS = MacOS...
    # Installs files necessary for the 'PyGame' library.
    os.system('pip3 install --user pygame')
    print("* Finished library install *")

if sys.platform == "win32":  # If the user's OS = Windows...
    os.system('pip install --user pygame')
    print("* Finished library install *")
"""
import pygame
print("* Using PyGame version", pygame.__version__.__str__(), "*")

x = 20
y = 200
width = 20
height = 20
vel = 5
loopBool = True


def setup():
    # Play background music
    pygame.mixer.init()
    bgmusic = ["audio/Sing_Swing_Bada_Bing.mp3",
    "audio/Tiptoe_Out_the_Back.mp3",
    "audio/Piano_Store.mp3"]
    pygame.mixer_music.load(bgmusic[0])  # This song is played first
    for i in range(1, len(bgmusic)):  # Queues the remaining songs
        pygame.mixer_music.queue(bgmusic[i])
        print("√ Queued song: ", bgmusic[i])
    pygame.mixer_music.set_volume(0.001)
    """ Volume is set to 1 at start of 'eventLoop'. This is done to avoid...
    a scratching noise when a song is loaded and played. """
    pygame.mixer_music.play(-1)

    # Create screen
    pygame.init()  # This line causes an APIS warning on MacOS. Check "Issues"
    screen = pygame.display.set_mode((1280, 800))
    pygame.display.set_caption('Shitty Blackjack')

    # Set background
    try:
        background = pygame.image.load("images/mainMenu.jpg").convert()
    except FileNotFoundError():
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((150, 0, 50))

    # Set cursor (optional)
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)

    # Blit to screen (render)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    eventLoop(screen, background)


def eventLoop(screen, background):
    global width, height, x, y, vel, loopBool
    pygame.mixer_music.set_volume(1)
    while loopBool:
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
        if keys[pygame.K_BACKSPACE]:
            loopBool = False

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height))
        pygame.display.update()


def main():
    setup()


main()  # Last line of code, runs main code.
