from sprite import Sprite
import pygame

#grass = pygame.image.load('src\\assets\\default_grass.png').convert()

class Void(Sprite):
    def __init__(self,pos):
        super().__init__(pos)
        self.img = pygame.image.load('src\\assets\\void.png').convert()

class Grass(Sprite):
    def __init__(self,pos):
        super().__init__(pos)
        self.img = pygame.image.load('src\\assets\\default_grass.png').convert()

class Farmland(Sprite):
    def __init__(self,pos):
        super().__init__(pos)
        self.img = pygame.image.load('src\\assets\\farmland.png').convert()

class Void(Sprite):
    def __init__(self,pos):
        super().__init__(pos)
        self.img = pygame.image.load('src\\assets\\void.png').convert()

class Tower(Sprite):
    def __init__(self,pos):
        super().__init__(pos)
        self.img = pygame.image.load('src\\assets\\higher.png').convert()


