
from pathlib import Path

class Settings:
    def __init__ (self) -> None:
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / "Assets" / "images" / "Starbasesnow.png"
        
        self.ship_file = Path.cwd() / "Assets" / "images" / "ship2(no bg).png"
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        
        self.bullet_file = Path.cwd() / "Assets" / "images" / "laserBlast.png"
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullets_amount = 5
        
        self.laser_sound = Path.cwd() / "Assets" / "sound" / "laser.mp3"
        