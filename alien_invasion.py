import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import ShipArsenal
from alien import Alien

class AlienInvasion:
 
    def __init__(self) -> None:
       
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
        
        # Main loop of the game
        while self.running:
            self._check_events()
            self.ship.update()
            self.alien.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
       
        # Update the screen with the latest game state
        self.screen.blit(self.bg, (0, 0))
        self.alien.draw_alien()
        self.ship.draw()        
        pygame.display.flip()

    def _check_events(self) -> None:
       
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
       
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _check_keydown_events(self, event) -> None:
       
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
    

