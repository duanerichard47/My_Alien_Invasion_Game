
import sys
import pygame

from erase_sideway_shooter_settings import Settings
from erase_sideway_shooter_ship import Ship
#from ship import Ship2
from erase_sideway_shooter_bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # Window Display:
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # #Full Screen Display  :      
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height



        pygame.display.set_caption("Duane's Alien Invasion Game")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()  #more than 1 bullet on screen at a time
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()    # Redraw the screen during each pass through the loop.     
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    def _check_keydown_events(self,event):
            """Respond to keypresses."""
            if event.key == pygame.K_UP:
                    self.ship.moving_up= True
            elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
            elif event.key == pygame.K_q:
                    sys.exit()
            elif event.key == pygame.K_SPACE:
                     self._fire_bullet()

    def _check_keyup_events(self, event):
            """Respond to key releases."""
            if event.key == pygame.K_UP:
                    self.ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
    
    def _fire_bullet(self):
            """Create a new bullet and add it to the bullets group."""
            if len(self.bullets) < self.settings.bullets_allowed:
                new_bullet = Bullet(self)
                self.bullets.add(new_bullet)

    def _update_bullets(self):
            """Update position of bullets and get rid of old bullets."""
            #Update bullet positions  
            self.bullets.update()
            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                #  Wrong : if bullet.rect.left > self.screen_rect.right:
                if bullet.rect.left > self.screen.get_rect().right:
                      self.bullets.remove(bullet)
            #print(len(self.bullets))         

    def _update_screen(self):
            """Update images on the screen, and flip to the new screen."""
            self.screen.fill (self.settings.bg_color)  
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
