import pygame # type: ignore
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player # type: ignore




def main():

    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
   
    updatable: pygame.sprite.Group = pygame.sprite.Group() 
    drawable: pygame.sprite.Group = pygame.sprite.Group() 

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)


        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
     
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        



if __name__ == "__main__":
    main()

