import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH 
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #initialze pygame and screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #print basic statements to console
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    #clock and dt
    clock = pygame.time.Clock()
    dt = 0

    #group calls
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #adding Player and Asteroid classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)

    #creating asteroid field object
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    #initialize player object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    #gameloop
    while True:
        #logging stuff
        log_state()

        #allows game to be quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #drawing the screen 60times per second
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

        
if __name__ == "__main__":
    main()
