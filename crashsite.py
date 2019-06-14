# -*- coding: utf-8 -*-
try:
    import sys
    import os
    import pygame
    print("* Using PyGame version", pygame.__version__.__str__(), "*")
except ImportError():
    if sys.platform == "darwin":  # If the user's OS = MacOS...
        # Installs files necessary for the 'PyGame' library.
        os.system('pip3 install --user pygame')
        print("* Finished library install *")

    if sys.platform == "win32":  # If the user's OS = Windows...
        os.system('pip install --user pygame')
        print("* Finished library install *")
    import sys
    import os
    import pygame
    print("* Using PyGame version", pygame.__version__.__str__(), "*")

# Colors
green = (0, 200, 0)
brightGreen = (70, 255, 70)

white = (255, 255, 255)
darkWhite = (200, 200, 200)

# Game variables
clock = pygame.time.Clock()
loopBool = True


def createButton(surface, font, msg, x, y, w, h, inClr, acClr):
    mousePos = pygame.mouse.get_pos()
    if x+w > mousePos[0] > x and y+h > mousePos[1] > y:
        pygame.draw.rect(surface, acClr, (x, y, w, h))
    else:
        pygame.draw.rect(surface, inClr, (x, y, w, h))

    playButton = pygame.Rect(x, y, w, h)
    playButtonText = font.render(str(msg), 1, (0, 0, 0))  # Create text
    playButtonTextRect = playButtonText.get_rect()  # Create figure for text
    playButtonTextRect.center = (playButton.centerx,
    playButton.centery)  # Set coords for the figure

    surface.blit(playButtonText, playButtonTextRect)


def loadMenu():
    # Prepare background music
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

    # Create screen
    pygame.init()  # This line causes an APIS warning on MacOS. Check "Issues"
    screen = pygame.display.set_mode((1280, 800))
    pygame.display.set_caption('Shitty Blackjack')

    # Set background
    background = pygame.image.load("images/mainMenu.jpg").convert()

    # Create buttons
    global green, brightGreen, white, darkWhite
    pygame.font.init()
    menuFont = pygame.font.Font("fonts/Good Brush.ttf", 40)  # Create font
    createButton(background, menuFont, "Play", 490, 310, 300, 90,
    brightGreen, green)
    createButton(background, menuFont, "Instructions", 490, 445, 300, 90,
    white, darkWhite)
    createButton(background, menuFont, "High Scores", 490, 580, 300, 90,
    white, darkWhite)

    # Set cursor (optional)
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)

    # Initial blit to screen (render)
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Play background music
    pygame.mixer_music.set_volume(0.75)
    pygame.mixer_music.play(-1)
    musicPlaying = True

    global loopBool  # Set to 'True' by default
    while loopBool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loopBool = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                    if musicPlaying:
                        pygame.mixer_music.pause()
                        musicPlaying = False
                    else:
                        pygame.mixer_music.unpause()
                        musicPlaying = True

        # Re-draw menu buttons
        createButton(background, menuFont, "Play", 490, 310, 300, 90,
        brightGreen, green)
        createButton(background, menuFont, "Instructions", 490, 445, 300, 90,
        white, darkWhite)
        createButton(background, menuFont, "High Scores", 490, 580, 300, 90,
        white, darkWhite)

        # Update 'background' on the main screen
        screen.blit(background, (0, 0))
        pygame.display.update()

        global clock
        clock.tick(60)  # Sets the FPS

    pygame.quit()


def main():
    loadMenu()

main()  # Last line of code, runs main code.
