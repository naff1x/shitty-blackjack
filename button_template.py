import pygame


class Button:
    def __init__(self, surface, f, msg, x, y, w, h, inClr, acClr):
        self.inactive_color = inClr
        self.active_color = acClr
        self.xPos = x
        self.yPos = y
        self.width = w
        self.height = h
        self.surface = surface
        """
        'win' --> window object
        'surface' --> surface within window to draw on
        'f' --> font to write text with
        'msg' --> message on button
        'x' and 'y' --> button position
        'w' and 'h' --> button dimensions
        'acClr' and 'inClr' --> button's color when hovered over and not
        """
        self.button = pygame.Rect(x, y, w, h)
        self.buttonText = f.render(str(msg), 1, (0, 0, 0))  # Create text
        self.buttonTextRect = self.buttonText.get_rect()  # Create figure for text
        self.buttonTextRect.center = (self.button.centerx,
        self.button.centery)  # Set coordinates for the figure

        surface.blit(self.buttonText, self.buttonTextRect)

    def engage_button(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.xPos + self.width > mouse_pos[0] > self.xPos and self.yPos + self.height > mouse_pos[1] > self.yPos:
            # Button engaged...
            pygame.draw.rect(self.surface, self.active_color, (self.xPos, self.yPos, self.width, self.height))
            self.surface.blit(self.buttonText, self.buttonTextRect)
        else:
            pygame.draw.rect(self.surface, self.inactive_color, (self.xPos, self.yPos, self.width, self.height))
            self.surface.blit(self.buttonText, self.buttonTextRect)
