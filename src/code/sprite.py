import pygame
import time


class Sprite:
    def __init__(self, pos, img, zoom):
        assert type(pos) == list

        self.x = pos[0]
        self.y = pos[1]
        self.offset = 0
        self.img = img
        self.last_zoom = zoom
        self.shadow_img = pygame.image.load(
            "src/assets/blocks/" + "shadow.png"
        ).convert()

        self.sprite = pygame.transform.scale(
            self.img, ((self.img.get_width() * zoom), (self.img.get_height() * zoom))
        )
        self.shadow = pygame.transform.scale(
            self.shadow_img,
            (
                (self.shadow_img.get_width() * zoom),
                (self.shadow_img.get_height() * zoom),
            ),
        )

    def draw(self, win, zoom, pos, height):
        if zoom != self.last_zoom:
            self.sprite = pygame.transform.scale(
                self.img,
                ((self.img.get_width() * zoom), (self.img.get_height() * zoom)),
            )
            self.shadow = pygame.transform.scale(
                self.shadow_img,
                (
                    (self.shadow_img.get_width() * zoom),
                    (self.shadow_img.get_height() * zoom),
                ),
            )
            self.last_zoom = zoom

        if height == 0:
            win.blit(
                self.shadow, (pos[0] - 32 * zoom, pos[1])  # pos  # -(self.offset*zoom)
            )
        win.blit(
            self.sprite,
            (  # pos
                pos[0] - 32 * zoom,
                pos[1]
                - (self.offset * zoom)
                - 32 * zoom
                - self.img.get_height() * zoom
                + 64 * zoom,
            ),
        )

    def update(self):
        self.offset -= 0.5
        self.offset = max(self.offset, 0)

    def get_pos(self):
        return [self.x, self.y]
