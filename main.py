from turtle import Screen
import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT



def initialize_pygame():
    pygame.init()

def display_set_mode():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen

def game_loop(screen):
    running = True
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()




# here starts the main execution

def main():
    print("Starting Asteroids with pygame version:", pygame.version.ver)
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    initialize_pygame()
    screen = display_set_mode()
    game_loop(screen)

if __name__ == "__main__":
    main()

