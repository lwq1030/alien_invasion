import pygame
from settings import Settings
from ship import Ship
import game_function as gf
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien")
    ship=Ship(ai_settings,screen)

    while True:
        gf.check_events(ship)
        ship.update() #根据标志状态实时更新飞船位置
        gf.update_screen(ai_settings,screen,ship)

run_game()