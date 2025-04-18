import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class ShipArsenal:
    def __init__(self, game: "AlienInvasion") -> None:
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
        
    def update_arsenal(self) -> None:
        self.arsenal.update()
        self.remove_bullet_offscreen(self.arsenal)
    
    def remove_bullet_offscreen(self, bullet: Bullet) -> None:
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)
        
    def draw(self) -> None:
        for bullet in self.arsenal:
            bullet.draw_bullet()
            
    def fire_bullet(self) -> None:
        if len(self.arsenal) < self.settings.bullets_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False