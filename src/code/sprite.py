import pygame
import time

class Sprite():
    def __init__(self, pos):
        assert(type(pos)==list)
        
        
        self.x = pos[0]
        self.y = pos[1]
        self.offset = 0
        

        self.img = None


    def draw(self, win, zoom, pos):
        sprite = pygame.transform.scale(self.img, ((self.img.get_width()*zoom),(self.img.get_height()*zoom)))
        win.blit(   #img
                    sprite,
                    (#pos
                        #self.cartesian_to_isometric(((self.x-wx)*zoom-64*zoom, (self.y-wy)*zoom-64*zoom))
                        pos[0]-32*zoom,
                        pos[1]-(self.offset*zoom)-32*zoom-self.img.get_height()*zoom+64*zoom
                    )
                )

    def get_pos(self):
        return [self.x, self.y]
        
    # Returns the center of the upper rectangle
    def get_middle(self):
        return [self.x-8, self.y-8]



        
 
    