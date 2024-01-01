import sys
import pygame

from settings import Settings
#class which manages game assets and behavior
class AlienInvasion:
    def __init__(self):
        #initialize the game and create game resources
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #sets the bg color
        self.bg_color = (55, 82, 155)

    def run_game(self):
        #starts the main loop for the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each pass through loop
            self.screen.fill(self.settings.bg_color)

            #make the most recently drawn screen visible
            pygame.display.flip()
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()