import sys
import pygame

from settings import Settings
from ship import Ship
#class which manages game assets and behavior
class AlienInvasion:
    def __init__(self):
        #initialize the game and create game resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #sets the bg color
        self.bg_color = (55, 82, 155)

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            #make the most recently drawn screen visible
            pygame.display.flip()

    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)
    def _check_keydown_events(self, event):
         if event.key == pygame.K_d:
                          #move the ship to the right
            self.ship.moving_right = True
         elif event.key == pygame.K_a:
            self.ship.moving_left = True
         elif event.key == pygame.K_ESCAPE:
             sys.exit()
    def _check_keyup_events(self, event):
         if event.key == pygame.K_d:
            self.ship.moving_right = False
                
         elif event.key == pygame.K_a:
            self.ship.moving_left = False              
    def run_game(self):
        #starts the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()