import pygame


class Ship():
    """A class to manage the ship."""

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.screen_rect =screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)