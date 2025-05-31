import sys
import pygame

from erase_star_settings import Settings
from erase_star_ship import Ship
#from ship import Ship2
from erase_star_bullet import Bullet
from erase_star_alien import Alien
from random import randint

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
 
        self.bullets = pygame.sprite.Group()  #more than 1 bullet on screen at a time
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color.
        #self.bg_color = (0, 0, 0)
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()
            self._update_screen()    # Redraw the screen during each pass through the loop.     
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                

            
    def _check_keydown_events(self,event):
                """Respond to keypresses."""
                if event.key == pygame.K_q:
                    sys.exit()
                
            

    

    def _create_fleet(self):
         """Create the fleet of aliens."""
         # Create an alien and keep adding aliens until there's no room left.
         # Spacing between aliens is one alien width and one alien height.    
         alien = Alien(self)   
         alien_width,  alien_height = alien.rect.size # size attribute has to be a tuple assigned to a tuple
         
         current_x = alien_width    #current_x is the total width in pixels of the fleet on x axis. A counter for loop.
         current_y = alien_height
         while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width #increases by space of 2 alien for new alien and a space
            # Finished a row, Loop end, reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.rect.x = x_position + self._get_star_offset() # position as int new_alien.rect. Alien left edge placed at end of fleet width
        new_alien.rect.y = y_position + self._get_star_offset()
        self.aliens.add(new_alien)

    def _get_star_offset(self):
        """Return a random adjustment to a star's position."""
        offset_size = 15
        return randint(-1*offset_size, offset_size)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill (self.settings.bg_color)  
        self.aliens.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    #Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
