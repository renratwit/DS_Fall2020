# TODO: put into main() method
from paddle import Paddle
from ball import Ball
import pygame


def main():
    pygame.init()

    pygame.display.set_caption("My Pong")
    # create surface
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15 
    VELOCITY = 1
    FPS = 300

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # fill background
    screen.fill((0, 0, 0))
    pygame.display.update()

    # draw walls
    wcolor = pygame.Color("white")
    bgcolor = pygame.Color("black")

    # # top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    # # left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    # # bottom
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, HEIGHT)))
    # pygame.draw.rect(screen, wcolor, pygame.Rect(screen, wcolor, pygame.Rect((0, HEIGHT), (WIDTH, HEIGHT-BORDER)))

    #Ball
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2

    vx = -VELOCITY
    vy = -VELOCITY
    b0 = Ball(x0, y0, vx, vy, screen, wcolor, bgcolor, [WIDTH, HEIGHT, BORDER])
    b0.show(wcolor)
    
    #Paddle
    p1 = Paddle()

    clock = pygame.time.Clock()

    # main loop
    running = True
    print(screen)

    pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        clock.tick(FPS)
        b0.update()


if __name__ == "__main__":
    # call the main function
    main()
