import pygame
from players import *
# import pygame_textinput
import button_template
from shitty_colors import *


class Game:
    def update_pts(self):
        user_pts = button_template.Button(self.game_background, self.comic_sans, str(self.user.hand.getValue()),
                                          200, 500, 100, 100, Colors.white, Colors.white)
        house_pts = button_template.Button(self.game_background, self.comic_sans, str(self.house.hand.getValue()),
                                          200, 200, 100, 100, Colors.white, Colors.white)
        if self.user.hand.getValue() > 21:  # Player has lost
            print("PLAYER HAS LOST")
        else:
            pass


    def blit_card(self, card, isPlayer):
        if isPlayer:  # If the given card is the player's card...
            self.game_background.blit(card.getVisual(), (self.user_cards_xpos, 450))
            self.user_cards_xpos += 40
        else:  # Given card belongs to the house...
            self.game_background.blit(card.getVisual(), (self.house_cards_xpos, 100))
            self.house_cards_xpos += 40

    def initial_draw(self):
        for i in range(2):
            card = self.deck.getTopCard()
            self.user.hit(card)
            self.blit_card(card, True)
            card = self.deck.getTopCard()
            self.house.hit(card)
            self.blit_card(card, False)

    def __init__(self, win, music_status):
        self.window = win
        self.game_background = pygame.image.load("images/blackjack-table.jpg").convert()
        self.user_cards_xpos = 500
        self.house_cards_xpos = 500

        # bet_input = pygame_textinput.TextInput("Enter bet here") # This line adds ~4s to the loading time

        # test_card = game_deck.newDeck[0].get_visual()
        # test_card = pygame.transform.scale(game_deck.deck[0].get_visual(), (130, 180))
        # game_background.blit(test_card, (545, 450))

        self.user = Player()
        self.house = Bank()

        self.deck = Deck()
        self.deck.shuffleDeck()

        self.initial_draw()

        # Add font
        self.comic_sans = pygame.font.Font("fonts/Comic Sans MS.ttf", 40)

        # Add buttons
        self.buttons = []
        self.hit_button = button_template.Button(self.game_background, self.comic_sans, "hit", 200, 355, 150, 90,
                                            Colors.bright_green, Colors.green)

        self.buttons.append(self.hit_button)

        self.update_pts()

        clock = pygame.time.Clock()
        game_active = True
        music_playing = music_status

        while game_active:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    game_active = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        if music_playing:
                            pygame.mixer_music.pause()
                            music_playing = False
                        else:
                            pygame.mixer_music.unpause()
                            music_playing = True
                if pygame.mouse.get_pressed()[0] and self.hit_button.button.collidepoint(pygame.mouse.get_pos()):
                    print("HIT")
                    card = self.deck.getTopCard()
                    self.user.hit(card)
                    self.blit_card(card, True)
                    self.update_pts()

                if event.type == pygame.MOUSEMOTION:  # When the mouse moves, check for engagement in each button
                    for i in range(len(self.buttons)):
                        self.buttons[i].engage_button()

            # Update 'gameBackground' on the main screen
            self.window.blit(self.game_background, (0, 0))

            """if bet_input.update(events):
                print(bet_input.get_text())

            window.blit(bet_input.get_surface(), (650, 775))"""

            pygame.display.update()
            clock.tick(60)  # Sets the FPS
