# Title: asteroid.py
# Author: Corey Greene
# Date Created: 13 June, 2026
# Last Update: 13 June, 2026
# Description: Astroid class file

import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    ASTEROID_MIN_RADIUS
)

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

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        x, y = self.position
        new_velocity_1 = self.velocity.rotate(angle)
        new_velocity_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(x, y, new_radius)
        new_asteroid_2 = Asteroid(x, y, new_radius)
        new_asteroid_1.velocity = new_velocity_1 * 1.2
        new_asteroid_2.velocity = new_velocity_2 * 1.2
