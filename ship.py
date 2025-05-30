import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen      #1 Bring in screen setting from AlienInvasion class
        self.screen_rect = ai_game.screen.get_rect()  #2 assign variable and create a rectangle

        #Load the ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()   #3  load ship image and place it in rectangle
        
        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom   #4 set surface ship rectangle coordinate to midbottom of screen

    def blitme(self):                       #5
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)

class Ship2:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen      #1 Bring in screen setting from AlienInvasion class
        self.screen_rect = ai_game.screen.get_rect()  #2 assign variable and create a rectangle

        #Load the ship image and get its rectangle
        self.image = pygame.image.load('images/redfighter0005.png')
        self.rect = self.image.get_rect()   #3  load ship image and place it in rectangle
        
        #Start each new ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center   #4 set surface ship rectangle coordinate to midbottom of screen

    def blitme(self):                       #5
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)