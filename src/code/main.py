import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()

from blocks import *
from window import Window
import time
import math

class Game():
    def __init__(self):
        self.win = Window()
        self.clock = pygame.time.Clock()
        # The position of a building in the list determines its drawing priority
        self.buildings = [[[Farmland([x*32+32,y*32+32], self.win.zoom) if x%4!=0 else Tower([x*32+32,y*32+32], self.win.zoom) for x in range(6)]for y in range(12) ]for z in range(3)]
        self.buildings[1][11][5] = Void([0,0],self.win.zoom)
    def draw(self):
        self.win.display.fill((40,45, 45))
        for i,col in enumerate(self.buildings):
            for j, row in enumerate(col):
                for h, building in enumerate(row):
                    # Check if inside view
                    coords = self.win.cart_to_iso([building.x, building.y])
                    if (coords[0] >= -128 and coords[0] <= self.win.WIN_X + 128) and (
                        coords[1] >= -128 and coords[1] <= self.win.WIN_Y + 128
                    ):
                        building.draw(self.win.display, self.win.zoom, self.win.cart_to_iso([building.x-i*26, building.y-i*26]), row,i)
        self.win.draw_terminal()
        pygame.display.flip()

    def input(self):
        #---Mouse-dependent---
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                self.win.quit = True
            if(event.type == pygame.MOUSEBUTTONDOWN):
                self.win.scroll(event.button)
                self.win.terminal.terminal_active(event)

                self.win.start_drag(event.button)
            if(event.type == pygame.MOUSEBUTTONUP):
                self.win.end_drag(event.button)
            self.win.terminal.terminal_input(event)  
        self.win.mouse_movement()
        
                
        #---Key-dependent---   
        self.highlight()
        keys = pygame.key.get_pressed() 
        self.win.move(keys)
        if keys[pygame.K_0]:
            self.win.win_x = 0
            self.win.win_y = 0
        if keys[pygame.K_ESCAPE]:
            self.win.quit = True
        if keys[pygame.K_F11]:
            self.win.toggle_fullscreen()

    def highlight(self):
        for col in self.buildings:
            for row in col:
                for building in row:
                    x,y = self.win.iso_to_cart(pygame.mouse.get_pos())
                    # Offset of 0*5 or 1*5, depends on condition
                    if (building.x>x>building.x-32 and building.y>y>building.y-32):
                        building.offset = 3

    def buildings_logic(self):
        for col in self.buildings:
            for row in col:
                for building in row:  
                    building.update()

    def update(self):
        self.input()
        self.buildings_logic()
        self.draw()
        self.clock.tick(60)

        
    def run(self):
            while(not self.win.quit): 
                self.update()          
            print("Stopping the game...")
              

if __name__ == '__main__':
    game = Game()
    game.run()
    
