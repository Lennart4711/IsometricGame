from sprite import Sprite
import pygame

# grass = pygame.image.load('src\\assets\\default_grass.png').convert()
path = "src/assets/blocks/"


class Void(Sprite):
    def __init__(self, pos, zoom):
        super().__init__(pos, pygame.image.load(path + "void.png").convert(), zoom)
        self.shadow_img = self.img
        self.shadow = pygame.transform.scale(
            self.shadow_img,
            (
                (self.shadow_img.get_width() * zoom),
                (self.shadow_img.get_height() * zoom),
            ),
        )


class Grass(Sprite):
    def __init__(self, pos, zoom):
        super().__init__(
            pos, pygame.image.load(path + "default_grass.png").convert(), zoom
        )


class Farmland(Sprite):
    def __init__(self, pos, zoom):
        super().__init__(pos, pygame.image.load(path + "farmland.png").convert(), zoom)


class Tower(Sprite):
    def __init__(self, pos, zoom):
        super().__init__(pos, pygame.image.load(path + "higher.png").convert(), zoom)
