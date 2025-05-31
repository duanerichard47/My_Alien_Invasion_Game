import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen      #1 Bring in screen setting from AlienInvasion class
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  #2 assign variable and create the screens rectangle

        #Load the ship image and get its rectangle
        self.image = pygame.image.load('images/Star pexels-nietjuhart-744973.jpg')
        self.rect = self.image.get_rect()   #3  load ship image and place it in rectangle
        
        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom  #4 You're aligning the ship's rect midbottom point with the midbottom point of the screen’s rectangle, ensuring the ship starts at the bottom center.

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # Movement flags; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Update the ship's position based on the movement flags."""
        #Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        #Update rect object from self.x
        self.rect.x = self.x

    def blitme(self):                       #5
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)