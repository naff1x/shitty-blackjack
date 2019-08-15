import pygame
import cards
# import pygame_textinput


class Game:
    def __init__(self, window, music_status):
        game_background = pygame.image.load("images/blackjack-table.jpg").convert()
        # bet_input = pygame_textinput.TextInput("Enter bet here") # This line adds ~4s to the loading time

        game_deck = cards.Deck()
        game_deck.shuffleDeck()
        # test_card = game_deck.newDeck[0].get_visual()
        test_card = pygame.transform.scale(game_deck.deck[0].get_visual(), (130, 180))
        game_background.blit(test_card, (545, 450))

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

            # Update 'gameBackground' on the main screen
            window.blit(game_background, (0, 0))

            """if bet_input.update(events):
                print(bet_input.get_text())

            window.blit(bet_input.get_surface(), (650, 775))"""

            pygame.display.update()
            clock.tick(60)  # Sets the FPS
