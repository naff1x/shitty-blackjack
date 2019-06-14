# -*- coding: utf-8 -*-
import sys
import os
try:
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


def createButton(win, surface, f, msg, x, y, w, h, inClr, acClr, action=None):
    global loopBool
    mousePos = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()
    if x+w > mousePos[0] > x and y+h > mousePos[1] > y:  # Button engaged...
        pygame.draw.rect(surface, acClr, (x, y, w, h))

        if mouseClick[0] == 1 and action is not None:  # Left mouse button...
            if action == "play game":
                print("! - STARTING GAME")
                loopBool = False
                startGame(win)
            elif action == "show instructions":
                print("! - SHOW INSTRUCTIONS")
                # loopBool = False
            elif action == "show scores":
                print("! - SHOW HIGH SCHORES")
                # loopBool = False
    else:
        pygame.draw.rect(surface, inClr, (x, y, w, h))

    playButton = pygame.Rect(x, y, w, h)
    playButtonText = f.render(str(msg), 1, (0, 0, 0))  # Create text
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
    menuBackground = pygame.image.load("images/mainMenu.jpg").convert()

    # Set cursor (optional)
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)

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

        # Draw buttons
        global green, brightGreen, white, darkWhite
        pygame.font.init()
        menuFont = pygame.font.Font("fonts/Good Brush.ttf", 40)  # Create font
        createButton(screen, menuBackground, menuFont, "Play", 490, 310, 300,
        90, brightGreen, green, "play game")
        createButton(screen, menuBackground, menuFont, "Instructions", 490,
        445, 300, 90, white, darkWhite, "show instructions")
        createButton(screen, menuBackground, menuFont, "High Scores", 490, 580,
        300, 90, white, darkWhite, "show scores")

        # Update 'menuBackground' on the main screen
        screen.blit(menuBackground, (0, 0))
        pygame.display.update()

        global clock
        clock.tick(60)  # Sets the FPS


def startGame(window):
    gameBackground = pygame.Surface(window.get_size())
    gameBackground = gameBackground.convert()
    gameBackground.fill((255, 0, 0))

    window.blit(gameBackground, (0, 0))
    pygame.display.flip()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


def main():
    loadMenu()

if __name__ == '__main__':
    main()

main()
