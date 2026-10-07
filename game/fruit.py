import random
import pygame

class Fruit:
    def __init__(self, screen_width):
        self.screen_width = screen_width
        self.radius = 14
        self.x = random.randint(30, screen_width - 30)
        self.y = -self.radius * 2
        self.speed = random.uniform(4.0, 6.5)

        self.is_hazard = random.random() < 0.2

        if self.is_hazard:
            self.color = (40, 40, 40)  # Rotten fruit / hazard
        else:
            self.color = random.choice([
        (230, 45, 45),   # Apple
        (245, 140, 30),  # Orange
        (160, 60, 200),  # Grape
    ])

    def update(self):
        self.y += self.speed

    def is_missed(self, screen_height):
        return self.y > screen_height

    @property
    def rect(self):
        return pygame.Rect(
            int(self.x - self.radius),
            int(self.y - self.radius),
            self.radius * 2,
            self.radius * 2,
        )

    def render(self, surface):
        center = (int(self.x), int(self.y))
        pygame.draw.circle(surface, self.color, center, self.radius)
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x - 4), int(self.y - 4)), 3)