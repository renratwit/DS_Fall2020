import pygame

class Ball:
    #pass

    #class variables
    RADIUS = 10
    vx = 1
    vy = 1

    def __init__(self, x, y, vx, vy, screen, fgcolor, bgcolor, dims):
        #instance variables
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screen = screen
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.dims = dims #array of screen dimensions. pygame probably has a method for it but I cant find it :\

    def show(self, color):
        pygame.draw.circle(self.screen, color, (self.x, self.y), self.RADIUS)
    
    def update(self):
        self.show(self.bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy


        #collision check
        px = self.x + self.vx
        py = self.y + self.vy
        #Hit right-wall
        if( ( px - self.RADIUS ) <= self.dims[2]):
            self.vx = -self.vx

        #hit top-wall
        if( ( py - self.RADIUS ) <= self.dims[2]):
            self.vy = -self.vy

        #hit bottom-wall
        if( ( py + self.RADIUS ) >= self.dims[1] - self.dims[2]):
            self.vy = -self.vy

        self.show(self.fgcolor)