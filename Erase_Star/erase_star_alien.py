import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """"Initiialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/Star pexels-nietjuhart-744973.jpg')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width  #When using x,y coordinents it based on center of rectangle. Default value x,y is zero
        self.rect.y = self.rect.height  # width and height means xy plotted somewhere on the screen width height number range

        #Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        
        # alien.rect.x = The alien's horizontal position(left edge, in pixels)
        # alien.rect.width = The alien's width(in pixels)(60pixels wide)
        # alien.rect.right =The x-coordinate of the right edge = rect.x + rect.width
        # alien.,rect.centerx = the x-coordinate of the horizontal center