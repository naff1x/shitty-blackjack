import pygame


class Button:
    def __init__(self, win, surface, f, msg, x, y, w, h, inClr, acClr):
        """
        'win' --> window object
        'surface' --> surface within window to draw on
        'f' --> font to write text with
        'msg' --> message on button
        'x' and 'y' --> button position
        'w' and 'h' --> button dimensions
        'acClr' and 'inClr' --> button's color when hovered over and not
        """
        mouse_pos = pygame.mouse.get_pos()
        if x+w > mouse_pos[0] > x and y+h > mouse_pos[1] > y:  # Button engaged...
            pygame.draw.rect(surface, acClr, (x, y, w, h))
        else:
            pygame.draw.rect(surface, inClr, (x, y, w, h))

        self.button = pygame.Rect(x, y, w, h)
        self.buttonText = f.render(str(msg), 1, (0, 0, 0))  # Create text
        self.buttonTextRect = self.buttonText.get_rect()  # Create figure for text
        self.buttonTextRect.center = (self.button.centerx,
        self.button.centery)  # Set coordinates for the figure

        surface.blit(self.buttonText, self.buttonTextRect)