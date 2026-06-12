# Title: main.py
# Author: Corey Greene
# Date Created: 11 June, 2026
# Last Update: 11 June, 2026
# Description: Asteroid game for Boot.dev

import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from circleshape import CircleShape
from player import Player

def main():
    # Initialize pygame and create the game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set Clock to 60 FPS
    clock = pygame.time.Clock()
    dt = 0.0

    # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Create the player
    Player.containers = (updatable, drawable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        #player.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        #player.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
