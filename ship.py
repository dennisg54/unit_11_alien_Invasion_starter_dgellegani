
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import ShipArsenal      

class Ship:
    """
    Class to manage the ship in the game.
    This class is responsible for the ship's position, movement, and firing bullets.
    The ship will be drawn on the screen and will respond to user input for movement and firing.
    The ship will also manage its arsenal of bullets, ensuring that the maximum number of bullets
    is not exceeded.
    """      
    def __init__ (self, game: "AlienInvasion", arsenal: "ShipArsenal") -> None:
        """
        Initialize the ship and set its starting position.
        The ship will be created at the bottom of the screen and will be able to move left and right.
        The ship will also be able to fire bullets, which will be managed by the ShipArsenal class.
        
        Args:
            game (AlienInvasion): The main game instance. This will allow the ship to access game settings and resources.
            arsenal (ShipArsenal): The ship's arsenal of bullets. This will allow the ship to manage its bullets and firing.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        
        self.arsenal = arsenal
        
    def update(self) -> None:
        """
        Update the ship's position based on user input.
        This method will be called in the game loop to ensure that the ship's position is updated based on the movement flags.
        The ship will move left or right based on the movement flags set by user input.        
        """
        # Update the ship's position based on the movement flags
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """
        Ship movement logic.
        This method will be called in the game loop to ensure that the ship's position is updated based on the movement flags.
        The ship will move left or right based on the movement flags set by user input.
        The ship's position will be updated based on the ship speed defined in the game settings.
        """
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed
        
        self.rect.x = self.x
        
    def draw(self) -> None:
        """
        Draw the ship on the screen.
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)
               
    def fire(self) -> bool:
        """
        Fire a bullet from the ship's arsenal.
        
        Returns:
            bool: True if a bullet was successfully fired, False otherwise.
        This method will check if the maximum number of bullets has been reached.
        """
        return self.arsenal.fire_bullet()
            
    