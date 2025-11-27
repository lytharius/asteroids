# asteroid.py
import pygame            # type: ignore

# Adjust this import to match where your base class actually lives.
# If circleshape.py is in the same directory as asteroid.py:
from circleshape import CircleShape
# (If it’s inside a package, e.g. mypkg/circleshape.py,
#  use: from mypkg.circleshape import CircleShape)

from constants import LINE_WIDTH

class Asteroid(CircleShape):
    """
    A circle that moves in a straight line.
    """

    def __init__(self, x: float, y: float, radius: int) -> None:
        super().__init__(x, y, radius)
        # Velocity will be set by the AsteroidField when it spawns an asteroid.
        self.velocity = pygame.Vector2(0, 0)

    # ------------------------------------------------------------------
    # Rendering
    # ------------------------------------------------------------------
    def draw(self, surface: pygame.Surface) -> None:
        """
        Draw a white circle with LINE_WIDTH outline.
        """
        pygame.draw.circle(
            surface,
            (255, 255, 255),                 # white
            (int(self.position.x), int(self.position.y)),
            self.radius,
            LINE_WIDTH
        )

    # ------------------------------------------------------------------
    # Physics / update
    # ------------------------------------------------------------------
    def update(self, dt: float) -> None:
        """
        Move the asteroid in a straight line with constant speed.
        `dt` is elapsed time since the last frame (in seconds).
        """
        self.position += self.velocity * dt
