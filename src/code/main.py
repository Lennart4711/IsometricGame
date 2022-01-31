import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

from blocks import *
from window import Window

class Game():
    def __init__(self):
        self.win = Window()
      
        self.buildings = [[Farmland([x*32+32,y*32+32]) if x%4!=0 else Tower([x*32+32,y*32+32]) for x in range(6)]for y in range(12)]
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

        for row in self.buildings:
            for building in row:
                building.draw(self.win.display, self.win.zoom, self.win.cart_to_iso([building.x, building.y]))
        pygame.display.flip()

    def input(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.win.quit = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                if event.button == 4 and self.win.zoom < self.win.MAX_ZOOM:
                    self.win.resize(1.1, self.win.screen_to_world(pygame.mouse.get_pos()))
                elif event.button == 5 and self.win.zoom > self.win.MIN_ZOOM:
                    self.win.resize(0.9, self.win.screen_to_world(pygame.mouse.get_pos()))    
                
        self.highlight()
        keys = pygame.key.get_pressed()   
        self.win.move(keys)

    def highlight(self):
        for row in self.buildings:
            for building in row:
                x,y = self.win.iso_to_cart(pygame.mouse.get_pos())
                if building.x>x>building.x-32 and building.y>y>building.y-32:
                    building.offset = 5
                else: 
                    building.offset = 0  

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
    
