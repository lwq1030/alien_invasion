import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
import game_function as gf
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien")
    ship=Ship(ai_settings,screen)
    bullets=Group()
    alien=Alien(ai_settings,screen)
    aliens=Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update() #根据标志状态实时更新飞船位置
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings,aliens)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)

run_game()