from math import dist
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()
from pygame.locals import *

from blocks import *
from sprite import Sprite
from custom_building import CustomBuilding

#TODO: higher tiles

class Game():
    def __init__(self):
        self.MIN_ZOOM = 0.035
        self.MAX_ZOOM = 50
        self.FIELD_SIZE = 2000
        self.WIN_X = 1000
        self.WIN_Y = 1000
        self.SPAWN_TIME = 0.5

        self.quit = False
        self.win = pygame.display.set_mode((self.WIN_X, self.WIN_Y))
        pygame.display.set_caption("CaMS")
        self.win_x = 0
        self.win_y = 0
        self.zoom = 3

        self.buildings = [[Farmland([x*32+32,y*32+32]) if x%4!=0 else Tower([x*32+32,y*32+32]) for x in range(6)]for y in range(12)]
        #kself.buildings[0][0] = Void([10,10])
        self.buildings[5][5] = Void([10,10])
        self.buildings[10][0] = Void([10,10])
        self.buildings[11][0] = Void([10,10])

        self.buildings[9][1] = Void([10,10])
        self.buildings[10][1] = Void([10,10])
        self.buildings[11][1] = Void([10,10])
        self.buildings[9][2] = Void([10,10])
        self.buildings[10][2] = Void([10,10])
        self.buildings[11][2] = Void([10,10])


        self.player = [0,0]

    def screen_to_world(self, pos):
        x = pos[0]/self.zoom+self.win_x
        y = pos[1]/self.zoom+self.win_y
        return [x,y]
    
    def cart_to_iso(self,cartesian):
        return  [
                    ((cartesian[0]-cartesian[1])-self.win_x)*self.zoom, 
                    ((cartesian[0]+cartesian[1])*0.5-self.win_y)*self.zoom
                ]

    def iso_to_cart(self,pos):
        x = pos[0]/self.zoom+self.win_x
        y = pos[1]/self.zoom+self.win_y
        return [
            (2*y+x)*0.5,
            (2*y-x)*0.5
        ]
    
    def world_to_screen(self, pos):
        x = (pos[0]-self.win_x)*self.zoom
        y = (pos[1]-self.win_y)*self.zoom
        return [x,y]

    def draw(self):
        self.win.fill((125,124, 110))

        coord = self.cart_to_iso(
                [self.player[0],
                self.player[1]])+[5*self.zoom, 5*self.zoom]

        for row in self.buildings:
            for building in row:
                building.draw(self.win, self.zoom, self.cart_to_iso([building.x, building.y]))

        pygame.draw.rect(self.win, (0,0,123), coord)
        pygame.display.flip()

    def input(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                #print("Stopping the game...")
                self.quit = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                before = self.screen_to_world(pygame.mouse.get_pos())

                if event.button == 4 and self.zoom < self.MAX_ZOOM:
                    self.resize(1.1, before)
                elif event.button == 5 and self.zoom > self.MIN_ZOOM:
                    self.resize(0.9, before)    
                
        for row in self.buildings:
            for building in row:
                x,y = self.iso_to_cart(pygame.mouse.get_pos())
                if building.x>x>building.x-32 and building.y>y>building.y-32:
                    building.offset = 5
                else: 
                    building.offset = 0
                


        keys = pygame.key.get_pressed()
                            
        self.move_player(keys)
        self.move(keys)

    def move_player(self, keys):
        if keys[pygame.K_w]:
                self.player[1] -=0.2*self.zoom
        elif keys[pygame.K_s]:
                self.player[1] +=0.2*self.zoom

        if keys[pygame.K_a]:
                self.player[0] -=0.2*self.zoom
        elif keys[pygame.K_d]:
                self.player[0] +=0.2*self.zoom

    def move(self, keys):
        if keys[pygame.K_LEFT]:
                self.win_x -=2/self.zoom
        elif keys[pygame.K_RIGHT]:
                self.win_x +=2/self.zoom

        if keys[pygame.K_UP]:
                self.win_y -=2/self.zoom
        elif keys[pygame.K_DOWN]:
                self.win_y += 2/self.zoom

    def resize(self, factor, before):
        self.zoom *= factor
        after = self.screen_to_world(pygame.mouse.get_pos())
        
        offset = before[0]-after[0],before[1]-after[1]
        self.win_x += offset[0]
        self.win_y += offset[1]

    def update(self):
        self.draw()
        self.input()
        
    def run(self):
            self.quit = False
            while(not self.quit): 
                self.update()
            

if __name__ == '__main__':
    game = Game()
    game.run()
    
