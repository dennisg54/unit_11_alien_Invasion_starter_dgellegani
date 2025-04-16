
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

class Bullet(Sprite):
    def __init__(self, game: "AlienInvasion") -> None:
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_w, self.settings.bullet_h))
        
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        
        self.y = float(self.rect.y)
        
    def update(self) -> None:
        # Move the bullet upwards
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self) -> None:
        # Draw the bullet on the screen
        self.screen.blit(self.image, self.rect)
        
