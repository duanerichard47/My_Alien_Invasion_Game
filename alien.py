import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """"Initiialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width  # width in pixels
        self.rect.y = self.rect.height  # height in pixels

        #Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
        
        # alien.rect.x = The alien's horizontal position(left edge, in pixels)
        # alien.rect.width = The alien's width(in pixels)(60pixels wide)
        # alien.rect.right =The x-coordinate of the right edge = rect.x + rect.width
        # alien.,rect.centerx = the x-coordinate of the horizontal center

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Move the alien to the right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction  #holds value of alien speed
        self.rect.x = self.x

    