import sys

import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #Initializes the game, settings, and creates a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    #Make a ship. bullets, and aliens.
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in.
    bullets = Group()
    aliens = Group()

    #Make an Alien
    alien = Alien(ai_settings, screen)

    #Make a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Create an isntance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Start the main loop for the game.
    while True:
        
        #Watches for keyboard and mouse movements
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)
            
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()