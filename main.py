import pygame # type: ignore
import sys                # needed for sys.exit()
from logger import log_event   # <-- new import
from constants import *
from logger import log_state
from player import Player # type: ignore
from asteroidfield import *

def main():

    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    updatable: pygame.sprite.Group = pygame.sprite.Group() 
    drawable: pygame.sprite.Group = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Check every asteroid against the player.
        # The `collides_with` method now encapsulates the math.
        for asteroid in asteroids:          # ``asteroids`` is a pygame.sprite.Group
            if asteroid.collides_with(player):
                log_event("player_hit")      # record the event
                print("Game over!")
                sys.exit()                   # terminate immediately

        updatable.update(dt)


        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
     
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        



if __name__ == "__main__":
    main()

