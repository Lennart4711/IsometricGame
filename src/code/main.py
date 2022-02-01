import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

from blocks import *
from window import Window
import time

class Game():
    def __init__(self):
        self.win = Window()
      
        self.buildings = [[Farmland([x*32+32,y*32+32], self.win.zoom) if x%4!=0 else Tower([x*32+32,y*32+32], self.win.zoom) for x in range(6)]for y in range(12)]
        self.buildings[5][5] = Void([10,10])
        self.buildings[10][0] = Void([10,10])
        self.buildings[11][0] = Void([10,10])
        self.buildings[9][1] = Void([10,10])
        self.buildings[10][1] = Void([10,10])
        self.buildings[11][1] = Void([10,10])
        self.buildings[9][2] = Void([10,10])
        self.buildings[10][2] = Void([10,10])
        self.buildings[11][2] = Void([10,10])

    def draw(self):
        self.win.display.fill((125,124, 110))

        i = 0

        for row in self.buildings:
            for building in row:
                # Check if inside view
                coords = self.win.cart_to_iso([building.x, building.y])
                if (coords[0] >= -128 and coords[0] <= self.win.WIN_X + 128) and (
                    coords[1] >= -128 and coords[1] <= self.win.WIN_Y + 128
                ):
                    # Why does it take so long with high zoom level
                    building.draw(self.win.display, self.win.zoom, self.win.cart_to_iso([building.x, building.y]))
                    i+=1

        
        pygame.display.flip()

    def input(self):
        #---Mouse-dependent---
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.win.quit = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                self.win.scroll(event.button)
                
        #---Key-dependent---   
        self.highlight()
        keys = pygame.key.get_pressed()   
        self.win.move(keys)
        

    def highlight(self):
        for row in self.buildings:
            for building in row:
                x,y = self.win.iso_to_cart(pygame.mouse.get_pos())
                # Offset of 0*5 or 1*5, depends on condition
                building.offset = (building.x>x>building.x-32 and building.y>y>building.y-32)*3
                

    def update(self):

        self.draw()
        self.input()

        
    def run(self):
            while(not self.win.quit): 
                self.update()          
            print("Stopping the game...")
              

if __name__ == '__main__':
    game = Game()
    game.run()
    
