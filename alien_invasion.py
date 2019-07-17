import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_function as gf
def run_game():
    pygame.init()
    ai_settings=Settings()
    stats=GameStats(ai_settings)

    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    sb = Scoreboard(ai_settings, screen, stats)
    pygame.display.set_caption("Alien")
    ship=Ship(ai_settings,screen)
    bullets=Group()
    alien=Alien(ai_settings,screen)
    aliens=Group()
    gf.creat_fleet(ai_settings,screen,ship,aliens)
    play_button=Button(ai_settings,screen,"Go")
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()  # 根据标志状态实时更新飞船位置
            gf.update_bullets(ai_settings, screen,stats,sb,ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen,stats,sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats,sb, ship, aliens, bullets, play_button)

run_game()