
class Settings:
    #A class to store all the settings for the game

    def __init__(self):
       
        self.screen_width = 1200
        self.screen_height = 800
        #self.bg_color = (255, 39, 225)
        self.bg_color = (129, 0, 255)
        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #ship speed
        self.ship_speed = 1