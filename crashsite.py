# -*- coding: utf-8 -*-
import sys
import os
try:
    import pygame_textinput
    import pygame
    print("* Using PyGame version", pygame.__version__.__str__(), "*")
except ImportError:
    if sys.platform == "darwin":  # If the user's OS is MacOS...
        # Installs files necessary for the 'PyGame' library.
        os.system('pip3 install --user pygame')
        print("* Finished library install *")

    if sys.platform == "win32":  # If the user's OS is Windows...
        os.system('pip install --user pygame')
        print("* Finished library install *")
    import pygame_textinput
    import pygame

    print("* Using PyGame version", pygame.__version__.__str__(), "*")

# Colors
green = (0, 200, 0)
brightGreen = (70, 255, 70)

white = (255, 255, 255)
darkWhite = (200, 200, 200)

red = (255, 0, 0)
darkRed = (255, 70, 70)

# Game variables
clock = pygame.time.Clock()
menuActive = True
gameActive = True
musicPlaying = True

# Fonts
pygame.font.init()
comicSans = pygame.font.Font("fonts/Comic Sans MS.ttf", 40)
goodBrush = pygame.font.Font("fonts/Good Brush.ttf", 40)


def createButton(win, surface, f, msg, x, y, w, h, inClr, acClr, action=None):
    global menuActive
    mousePos = pygame.mouse.get_pos()
    mouseClick = pygame.mouse.get_pressed()
    if x+w > mousePos[0] > x and y+h > mousePos[1] > y:  # Button engaged...
        pygame.draw.rect(surface, acClr, (x, y, w, h))

        if mouseClick[0] == 1 and action is not None:  # Left mouse button...
            if action == "actionGame":
                print("! - STARTING GAME")
                menuActive = False
                startGame(win)
            elif action == "actionInstructions":
                print("! - SHOW INSTRUCTIONS")
                # menuActive = False
            elif action == "actionScores":
                print("! - SHOW HIGH SCHORES")
                # menuActive = False
            elif action == "actionHit":
                print("! - PLAYER HAS HIT")
            elif action == "actionStand":
                print("! - PLAYER HAS STOOD")
            else:
                print("! - BUTTON HAS NO SET ACTION")
    else:
        pygame.draw.rect(surface, inClr, (x, y, w, h))

    playButton = pygame.Rect(x, y, w, h)
    playButtonText = f.render(str(msg), 1, (0, 0, 0))  # Create text
    playButtonTextRect = playButtonText.get_rect()  # Create figure for text
    playButtonTextRect.center = (playButton.centerx,
    playButton.centery)  # Set coords for the figure

    surface.blit(playButtonText, playButtonTextRect)


def loadMenu():
    pygame.init()  # This line causes an APIS warning on MacOS. Check "Issues"
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
    screen = pygame.display.set_mode((1280, 800))
    pygame.display.set_caption('Shitty Blackjack')

    # Set background
    menuBackground = pygame.image.load("images/mainMenu.jpg").convert()

    # Set cursor (optional)
    pygame.mouse.set_cursor(*pygame.cursors.broken_x)

    # Play background music
    pygame.mixer_music.set_volume(0.75)
    pygame.mixer_music.play(-1)

    global menuActive, musicPlaying  # Set to 'True' by default
    while menuActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuActive = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    if musicPlaying:
                        pygame.mixer_music.pause()
                        musicPlaying = False
                    else:
                        pygame.mixer_music.unpause()
                        musicPlaying = True

        # Draw buttons
        global green, brightGreen, white, darkWhite, comicSans, goodBrush
        createButton(screen, menuBackground, comicSans, "Play", 490, 310, 300,
        90, brightGreen, green, "actionGame")
        createButton(screen, menuBackground, comicSans, "Instructions", 490,
        445, 300, 90, white, darkWhite, "actionInstructions")
        createButton(screen, menuBackground, comicSans, "High Scores", 490,
        580, 300, 90, white, darkWhite, "actionScores")

        # Update 'menuBackground' on the main screen
        screen.blit(menuBackground, (0, 0))
        pygame.display.update()

        global clock
        clock.tick(60)  # Sets the FPS


def startGame(window):
    gameBackground = pygame.image.load("images/blackjack-table.jpg").convert()
    betInput = pygame_textinput.TextInput("Enter bet here")
    window.blit(gameBackground, (0, 0))
    pygame.display.flip()
    global gameActive, musicPlaying  # Set to 'True' by default
    while gameActive:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    if musicPlaying:
                        pygame.mixer_music.pause()
                        musicPlaying = False
                    else:
                        pygame.mixer_music.unpause()
                        musicPlaying = True

        global comicSans, goodBrush, brightGreen, green, red, darkRed
        createButton(window, gameBackground, comicSans, "hit", 240, 360, 140,
        60, brightGreen, green, "actionHit")
        createButton(window, gameBackground, comicSans, "stand", 900, 360, 140,
        60, red, darkRed, "actionStand")

        # Update 'gameBackground' on the main screen
        window.blit(gameBackground, (0, 0))
        # betInput.update(events)
        if betInput.update(events):
            print(betInput.get_text())
        window.blit(betInput.get_surface(), (650, 775))
        pygame.display.update()

        global clock
        clock.tick(60)  # Sets the FPS


def main():
    loadMenu()

if __name__ == '__main__':
    main()

main()
