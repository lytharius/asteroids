# asteroid.py
import pygame            # type: ignore
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: int) -> None:
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(
            surface,
            (255, 255, 255),                 # white
            (int(self.position.x), int(self.position.y)),
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        # Zerstöre das aktuelle Objekt
        self.kill()

        # Kein Split, wenn es schon klein ist
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Split erzeugen
        log_event("asteroid_split")                      # Log‑Event

        # Zufälliger Winkel zwischen 20° und 50°
        angle = random.uniform(20, 50)

        # Neue Geschwindigkeitsvektoren (gegenläufig)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)

        # Radius für die kleineren Asteroiden
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Zwei neue Asteroiden an der gleichen Position erzeugen
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Geschwindigkeit vergrößern (x 1.2)
        asteroid1.velocity = vec1 * 1.2
        asteroid2.velocity = vec2 * 1.2