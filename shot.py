import pygame                   # type: ignore
from circleshape import CircleShape  
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(
            x=x,
            y=y,
            radius=SHOT_RADIUS,
        )
        self.velocity = pygame.math.Vector2(0, 0)
        self.x = x          
        self.y = y
        self.color = (255, 255, 0)  # Yellow

    def draw(self, surface: pygame.Surface):
        pygame.draw.circle(
            surface,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )

    def update(self, dt: float):
        super().update(dt)   
        self.x = self.position.x
        self.y = self.position.y

