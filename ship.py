import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self,ai_setting,screen):
        """Initialize the ship and set its starting position."""
        super(Ship,self).__init__()
        self.screen = screen
        self.ai_setting=ai_setting
        self.screen_rect =screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.center=float(self.rect.centerx)
        self.moving_right=False
        self.moving_left=False
    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
        #if self.moving_right:
            self.center+=self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center-=self.ai_setting.ship_speed_factor
        self.rect.centerx=self.center

    def center_ship(self):
        self.center=self.screen_rect.centerx

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)