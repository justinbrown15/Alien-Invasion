import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
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
        self.bullets = pygame.sprite.Group()
        #sets the bg color
        #self.bg_color = (55, 82, 155)
        self.bg_color = (129, 0, 255)

        

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
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
         elif event.key == pygame.K_SPACE:
             self._fire_bullet()
         elif event.key == pygame.K_ESCAPE:
             sys.exit()
    def _check_keyup_events(self, event):
         if event.key == pygame.K_d:
            self.ship.moving_right = False
                
         elif event.key == pygame.K_a:
            self.ship.moving_left = False
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                print(len(self.bullets))            
    def run_game(self):
        #starts the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            #gets rid of bullets that have disappeared off the screen
            
            


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()