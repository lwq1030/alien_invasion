class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.bullet_width= 999#3
        self.bullet_heigth=15
        self.bullet_color=60,60,60
        self.bullets_allowed=3
        self.alien_speed_factor=1
        self.fleet_drop_speed=10
        self.fleet_direction=1 #1为向右，-1为向左
        self.ship_limit=1
        self.speedup_scale=1.1
        self.initialized_dynamic_settings()
        self.alien_points = 50
        self.score_scale=1.5

    def initialized_dynamic_settings(self):
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=1
        self.fleet_direction=1

    def increase_speed(self):
        self.ship_speed_factor*=self.speedup_scale
        self.bullet_speed_factor*=self.speedup_scale
        self.alien_speed_factor*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        #print(self.alien_points)

