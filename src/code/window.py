import pygame
class Window():
    def __init__(self):
        self.win_x = 0
        self.win_y = 0
        self.zoom = 3
        self.MIN_ZOOM = 0.035
        self.MAX_ZOOM = 50
        self.FIELD_SIZE = 2000
        self.WIN_X = 1000
        self.WIN_Y = 1000
        self.display = pygame.display.set_mode((self.WIN_X, self.WIN_Y))
        pygame.display.set_caption("CaMS")
        self.quit = False

    def resize(self, factor, before):
        self.zoom *= factor
        after = self.screen_to_world(pygame.mouse.get_pos())
        
        offset = before[0]-after[0],before[1]-after[1]
        self.win_x += offset[0]
        self.win_y += offset[1]

    def move(self, keys):
        if keys[pygame.K_LEFT]:
                self.win_x -=2/self.zoom
        elif keys[pygame.K_RIGHT]:
                self.win_x +=2/self.zoom

        if keys[pygame.K_UP]:
                self.win_y -=2/self.zoom
        elif keys[pygame.K_DOWN]:
                self.win_y += 2/self.zoom

    def screen_to_world(self, pos):
        x = pos[0]/self.zoom+self.win_x
        y = pos[1]/self.zoom+self.win_y
        return [x,y]

    def world_to_screen(self, pos):
        x = (pos[0]-self.win_x)*self.win.zoom
        y = (pos[1]-self.win_y)*self.win.zoom
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
