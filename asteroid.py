# Title: asteroid.py
# Author: Corey Greene
# Date Created: 13 June, 2026
# Last Update: 13 June, 2026
# Description: Astroid class file

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

# CircleShape
# |_ Asteroid
# |_ Player

class Asteroid(CircleShape):
    containers: tuple[pygame.sprite.Group, ...]

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += (self.velocity * dt)