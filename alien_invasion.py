import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import ShipArsenal
from alien import Alien

class AlienInvasion:
    """
    Main class for the Alien Invasion game.
    This class is responsible for initializing the game, creating resources,
    and managing the game loop.
    """
    def __init__(self) -> None:
        """
        Initialize the game and create resources.
        This includes setting up the screen, loading images, and initializing
        the game clock.
        """
        # Initialize the game and create resources
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)
        
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))
                
        self.running = True
        self.clock = pygame.time.Clock()
        
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.5)

        self.ship = Ship(self, ShipArsenal(self))
        self.alien = Alien(self, 10, 10)

    def run_game(self) -> None:
        """
        Start the main loop for the game.
        This loop will continue until the game is exited.
        It will check for events, update the game state, and render the screen.
        """
        # Main loop of the game
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        """
        Update the screen with the latest game state.
        This method will clear the screen, draw the background, and then draw the ship.
        Finally, it will update the display to show the new frame.        
        """
        # Update the screen with the latest game state
        self.screen.blit(self.bg, (0, 0))
        self.alien.draw_alien()
        self.ship.draw()        
        pygame.display.flip()

    def _check_events(self) -> None:
        """
        Check for keyboard and mouse events.
        This method will handle events such as quitting the game, moving the ship,
        and firing bullets.
        """
        # Check for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                

    def _check_keyup_events(self, event) -> None:
        """
        Check for key release events.
        This method will handle events such as stopping the ship movement when
        the arrow keys are released.

        Args:
            event (key release): The event object containing information about the key released.
        This method will check if the released key is the right or left arrow key and stop the ship's movement accordingly.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _check_keydown_events(self, event) -> None:
        """
        Check for key press events. 
        
        Args:
            event (key press): The event object containing information about the key pressed.
        This method will check if the pressed key is the right or left arrow key and start moving the ship accordingly.
        It will also check if the space bar is pressed to fire a bullet and if the 'q' key is pressed to quit the game.
        It will also play the laser sound when the space bar is pressed.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
               self.laser_sound.play()
               self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
            
    
    
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
    

