import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien, self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load('image/alien.bmp')
        self.rect=self.image.get_rect()
        #外星人出生在屏幕左上角
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)
