# TODO: put into main() method

import pygame


def main():
    pygame.init()

    pygame.display.set_caption("My Pong")
    # create surface
    WIDTH = 800
    HEIGHT = 400
    BORDER = 15

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # fill background
    screen.fill((0, 0, 0))
    pygame.display.update()

    # draw walls
    wcolor = pygame.Color("white")

    # # top wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    # # left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    # # bottom
    pygame.draw.rect(screen, wcolor, pygame.Rect(
        (0, HEIGHT-BORDER), (WIDTH, HEIGHT)))
    # pygame.draw.rect(screen, wcolor, pygame.Rect(screen, wcolor, pygame.Rect((0, HEIGHT), (WIDTH, HEIGHT-BORDER)))

    pygame.display.update()
    # main loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    # call the main function
    main()
