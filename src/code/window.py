import pygame
from terminal import Terminal

class Window():
    def __init__(self):
        self.fullscreen = False
        self.win_x = 0
        self.win_y = 0
        self.zoom = 3
        self.MIN_ZOOM = 1.5
        self.MAX_ZOOM = 4
        self.input_width = 600
        self.WIN_X = 2700-self.input_width
        self.WIN_Y = 1100
        
        self.display = pygame.display.set_mode((self.WIN_X+self.input_width,self.WIN_Y))
        pygame.display.set_caption("IsoGame")
        self.quit = False
        self.terminal = Terminal(self)
        #self.box = pygame.Rect(0, 0, self.WIN_X,self.WIN_Y)
        self.drag_pos = (0,0)
        self.started = False

    def toggle_fullscreen(self):
        if self.fullscreen:
            self.fullscreen = False
            self.display = pygame.display.set_mode((self.WIN_X+self.input_width,self.WIN_Y))
        else:
            self.fullscreen = True
            self.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)


    def resize(self, factor, before):
        self.zoom *= factor
        after = self.screen_to_world(pygame.mouse.get_pos())
        
        offset = before[0]-after[0],before[1]-after[1]
        self.win_x += offset[0]
        self.win_y += offset[1]

    def move(self, keys):
        if keys[pygame.K_LEFT]:
                self.win_x -=4/(self.zoom)
        elif keys[pygame.K_RIGHT]:
                self.win_x +=4/(self.zoom)

        if keys[pygame.K_UP]:
                self.win_y -=4/(self.zoom)
        elif keys[pygame.K_DOWN]:
                self.win_y += 4/(self.zoom)

    def start_drag(self, button):
        if button == 1 and not self.started and pygame.mouse.get_pos()[0]<self.WIN_X:
            self.drag_pos = pygame.mouse.get_pos()
            self.started = True
    
    def end_drag(self, button):
        if button == 1 and self.started:
            self.started = False
    
    def mouse_movement(self):
        if self.started:
            self.win_x += (self.drag_pos[0]-pygame.mouse.get_pos()[0])/self.zoom
            self.win_y += (self.drag_pos[1]-pygame.mouse.get_pos()[1])/self.zoom
            self.drag_pos = pygame.mouse.get_pos()

        
    def scroll(self,button):
        if(pygame.mouse.get_pos()[0]<self.WIN_X):
            if button == 4 and self.zoom < self.MAX_ZOOM:
                self.resize(1.1, self.screen_to_world(pygame.mouse.get_pos()))
            elif button == 5 and self.zoom > self.MIN_ZOOM:
                self.resize(0.9, self.screen_to_world(pygame.mouse.get_pos()))    

    def screen_to_world(self, pos):
        x = pos[0]/self.zoom+self.win_x
        y = pos[1]/self.zoom+self.win_y
        return [x,y]

    def world_to_screen(self, pos):
        x = (pos[0]-self.win_x)*self.zoom
        y = (pos[1]-self.win_y)*self.zoom
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

    def draw_terminal(self):
        self.terminal.draw(self)