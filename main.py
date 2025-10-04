import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers =  (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000.0
       
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                import sys
                sys.exit()

        for asteroid in list(asteroids):
            hit = False
            for shot in list(shots):
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()
                    hit = True
                    break
            if hit:
                continue
        
        screen.fill("black")
       
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
