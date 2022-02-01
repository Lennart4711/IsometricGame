import pygame

class Sprite():
    def __init__(self, pos, img, zoom):
        assert(type(pos)==list)

        self.x = pos[0]
        self.y = pos[1]
        self.offset = 0
        self.img = img
        self.last_zoom = 3
        self.sprite = pygame.transform.scale(self.img, ((self.img.get_width()*zoom),(self.img.get_height()*zoom)))

    def draw(self, win, zoom, pos):
        if zoom!=self.last_zoom:
            self.sprite = pygame.transform.scale(self.img, ((self.img.get_width()*zoom),(self.img.get_height()*zoom)))
            self.last_zoom = zoom
        
        win.blit(
                    self.sprite,
                    (#pos
                        #self.cartesian_to_isometric(((self.x-wx)*zoom-64*zoom, (self.y-wy)*zoom-64*zoom))
                        pos[0]-32*zoom,
                        pos[1]-(self.offset*zoom)-32*zoom-self.img.get_height()*zoom+64*zoom
                    )
                )
        
    def get_pos(self):
        return [self.x, self.y]
        



        
 
    