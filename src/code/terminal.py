import pygame
pygame.font.init()
class Terminal():
    def __init__(self, win):
        self.history = []
        self.history_surface = []
        self.myfont = pygame.font.SysFont('awdas', 30)
        self.dollar = self.myfont.render('$', True, (200, 200, 200))
        self.active = False
        self.input_box = pygame.Rect(win.WIN_X+25, win.WIN_Y-40, 600,60)
        self.text = ""
        self.inputsurface  = self.myfont.render(self.text, True, (200, 200, 200))
        self.command_list = ["mv", "clear", "touch", "cat", "help"]
        self.unknown = self.myfont.render('Unknown command - type "help" for help', True, (200, 200, 200))

        
    def draw(self,win):
        pygame.draw.rect(win.display, (25,25,25), (win.WIN_X, 0, 600,win.WIN_Y)) # Big rect
        pygame.draw.rect(win.display, (40,40,40), (win.WIN_X, win.WIN_Y-60, 600,60)) # Input-background
        pygame.draw.rect(win.display, (120,120,120) if self.active else (60,60,60), (win.WIN_X, win.WIN_Y-60, 600,60),5) # Input-Border
        win.display.blit(self.dollar,(win.WIN_X+10,win.WIN_Y-40)) # $ sign
        self.inputsurface  = self.myfont.render(self.text, True, (200, 200, 200))

        win.display.blit(self.inputsurface, (self.input_box.x, self.input_box.y))
        y = 20
        for command in self.history:
            textsurface  = self.myfont.render("> "+command, True, (200, 200, 200))
            win.display.blit(textsurface,(win.WIN_X+10,y))
            y += 30
            if command != "" and command.partition(' ')[0] not in self.command_list:
                win.display.blit(self.unknown,(win.WIN_X+10,y))
                y+=30

            
        
    
    def terminal_active(self, event):
        if event.button == 1:
            self.active = bool(self.input_box.collidepoint(event.pos))
    
    def terminal_input(self, event):
        if event.type != pygame.KEYDOWN:
            return
        if self.active:
            if event.key == pygame.K_RETURN:
                self.history.append(self.text)
                if self.text == "clear":
                    self.history = []
                self.text = ''
                if len(self.history)>=15:
                    del self.history[0]

            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif self.inputsurface.get_width() < 500:
                self.text += event.unicode
                
