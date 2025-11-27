import pygame                   # type: ignore
from circleshape import CircleShape   # <-- adjust if your file is named differently
from constants import SHOT_RADIUS

class Shot(CircleShape):
    """
    A simple bullet that flies straight in the direction it was fired.
    Inherits from `CircleShape` so we only need to override draw/update.
    """

    def __init__(self, x: float, y: float):
        super().__init__(
            x=x,
            y=y,
            radius=SHOT_RADIUS,
                    
        )
        self.velocity = pygame.math.Vector2(0, 0)
        self.x = x          # integer/float coordinates for the bullet centre
        self.y = y
        self.color = (255, 255, 0)  # Yellow

    def draw(self, surface: pygame.Surface):
        """Draw the bullet as a filled circle."""
        pygame.draw.circle(
            surface,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )

    def update(self, dt: float):
        """
        Move the shot according to its velocity.
        `dt` is the time passed in seconds.
        """
        super().update(dt)   # CircleShape.update already moves the sprite