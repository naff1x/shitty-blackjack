# -*- coding: utf-8 -*-
import sys
import os
import button_template
from shitty_colors import *
import game

try:
    import pygame
    import pygame_textinput

    print("* Using PyGame version", pygame.__version__.__str__(), "*")
except ImportError:
    if sys.platform == "darwin":  # If the user's OS is MacOS...
        # Installs files necessary for the 'PyGame' library.
        os.system('pip3 install --user pygame')
        print("* Finished library install *")

    if sys.platform == "win32":  # If the user's OS is Windows...
        os.system('pip install --user pygame')
        print("* Finished library install *")
    import pygame
    import pygame_textinput

    print("* Using PyGame version", pygame.__version__.__str__(), "*")


class Menu:
    def __init__(self):
        pygame.init()  # This line causes an APIS warning on MacOS. Check "Issues"
        clock = pygame.time.Clock()

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
        menu_background = pygame.image.load("images/mainMenu.jpg").convert()

        # Set cursor (optional)
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)

        # Play background music
        pygame.mixer_music.set_volume(0.75)
        pygame.mixer_music.play(-1)

        # Fonts
        pygame.font.init()
        comic_sans = pygame.font.Font("fonts/Comic Sans MS.ttf", 40)

        # Add buttons (not rendered yet)
        play_button = button_template.Button(menu_background, comic_sans, "Play", 490, 310, 300, 90,
                               Colors.bright_green, Colors.green)

        menu_active = True
        music_playing = True

        while menu_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menu_active = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        if music_playing:
                            pygame.mixer_music.pause()
                            music_playing = False
                        else:
                            pygame.mixer_music.unpause()
                            music_playing = True
                if pygame.mouse.get_pressed()[0] and play_button.button.collidepoint(pygame.mouse.get_pos()):
                    menu_active = False
                    print("GAME STARTING")
                    game.Game(screen, music_playing)

            button_template.Button(menu_background, comic_sans, "Play", 490, 310, 300, 90,
                                   Colors.bright_green, Colors.green)
            """
            button_template.Button(menu_background, comic_sans, "Instructions", 490, 445, 300, 90,
                                   Colors.white, Colors.dark_white)
            button_template.Button(menu_background, comic_sans, "High Scores", 490, 580, 300, 90,
                                   Colors.white, Colors.dark_white)
            """

            # Update 'menuBackground' on the main screen
            screen.blit(menu_background, (0, 0))
            pygame.display.update()

            clock.tick(60)  # Sets the FPS


Menu()
