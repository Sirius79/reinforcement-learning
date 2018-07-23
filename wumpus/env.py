import pygame
import random
import math
import numpy as np
import matplotlib.pyplot as plt

'''
    map:
    xxxxxxxxxxxx
    x...bpbg.twx
    x....bgdg.tx
    x...bpbg...x
    x....b.b...x
    x...b.bpb..x
    x..bpb.bpb.x
    x.bpb.bpb..x
    x..b...b...x
    x.bpb.bpb..x
    xs.bpb.b...x
    xxxxxxxxxxxx

    x = wall
    s = start
    d = destination
    b = breeze
    p = pit
    g = glitter
    t = stench
    w = wumpus
    
'''

mapcolors = \
{'x': (100, 60, 30),
 'd': (30, 120, 10),
 'p': (255, 255, 255),
 'b': (0, 0, 0),
 'g': (10, 10, 10),
 't': (20, 20, 20),
 'w': (30, 30, 30)}

class Environment(object):

    def __init__(self, width=720, height=540):
        '''
            Initialize pygame, window, background
        '''
        pygame.init()
        logo = pygame.image.load("wumpus.jpg")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Wumpus World")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()

    def run(self):
        '''
            Main loop
        '''
        #variable to control main loop
        running = True

        #main loop
        while running:
            #event handling from event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    #user presses escape key
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))

        pygame.quit()
        
if __name__=="__main__":
    Environment().run()
