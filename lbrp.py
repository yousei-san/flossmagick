# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys, os

#earth = "🜃"
#water = "🜄"
#air = "🜁"
#fire = "🜂"

def waitforpress():
    pygame.event.clear()
    boolean = True
    while boolean:
         wait = pygame.event.wait()
         if wait.type == KEYDOWN and wait.key != K_q or wait.type == MOUSEBUTTONDOWN:
             boolean = False
         elif wait.type == QUIT:
             pygame.quit()
             sys.exit(0)
         elif wait.type == KEYDOWN and wait.key == K_q:
             pygame.quit()
             sys.exit(0)
    return

def earth(floor,height,width):
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+x,height/2),(width/2+x,height/2),2)
            pygame.display.update()
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+x/2,height/2+x/2),(width/2+x/2,height/2+x/2),2)
            pygame.display.update()
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+15+x/2,height/2+15-x/2),(width/2+15+x/2,height/2+15-x/2),2)
            pygame.display.update()
        waitforpress()
        for x in range(26):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+2+x,height/2+7),(width/2+7+x,height/2+7),2)
            pygame.display.update()
        return

def water(floor,height,width):
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(61, 80, 245, 1),(width/2+30+x,height/2),(width/2+30+x,height/2),2)
            pygame.display.update()
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(61, 80, 245, 1),(width/2+30+x/2,height/2+x/2),(width/2+30+x/2,height/2+x/2),2)
            pygame.display.update()
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(61, 80, 245, 1),(width/2+30+15+x/2,height/2+15-x/2),(width/2+30+15+x/2,height/2+15-x/2),2)
            pygame.display.update()
        return

def air(floor,height,width):
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+x,height/2-30),(width/2+x,height/2-30),2)
            pygame.display.update()
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+x/2,height/2+x/2-30),(width/2+x/2,height/2+x/2-30),2)
            pygame.display.update()
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+15+x/2,height/2+15-x/2-30),(width/2+15+x/2,height/2+15-x/2-30),2)
            pygame.display.update()
        waitforpress()
        for x in range(26):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+2+x,height/2+7-30),(width/2+7+x,height/2+7-30),2)
            pygame.display.update()
        return

def fire(floor,height,width):
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+x,height/2),(width/2+x,height/2),2)
            pygame.display.update()
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+x/2,height/2+x/2),(width/2+x/2,height/2+x/2),2)
            pygame.display.update()
        waitforpress()
        for x in range(30):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+15+x/2,height/2+15-x/2),(width/2+15+x/2,height/2+15-x/2),2)
            pygame.display.update()
        waitforpress()
        for x in range(26):
            pygame.draw.line(floor,pygame.Color(76,175,80,1),(width/2+2+x,height/2+7),(width/2+7+x,height/2+7),2)
            pygame.display.update()
        return

def main():
    pygame.init()
    height = 640
    width = 480
    floor = pygame.display.set_mode((height, width))
    pygame.display.set_caption('Lesser Banishing Ritual of the pentagram')
    background = pygame.Surface(floor.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    #clock = pygame.time.Clock()
    edraw = True
    wdraw = True
    adraw = True
    running = True
    while running:
        #clock.tick(5)
        #draw the altar one keypress at a time
        if edraw:
            earth(floor,height,width)
        edraw = False
        waitforpress()
        if wdraw:
            water(floor,height,width)
        wdraw = False
        waitforpress()
        if adraw:
            air(floor,height,width)
        waitforpress()
        #floor.blit(background, (0, 0))
        pygame.display.update()
    pygame.quit()
    exit()


if __name__ == '__main__': main()

#pygame
