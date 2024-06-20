from config import COLOR

import pygame
from pygame import Surface

from block import Block


class Cobblestone(Block):
    id = "cobblestone"

    @staticmethod
    def get_surface():
        surface = Surface((80, 80))
        surface.fill(COLOR.BACKGROUND)

        dark_gray = (105, 105, 105)
        light_gray = (192, 192, 192)
        stones = [
            (0, 0, 30, 30, dark_gray),
            (20, 0, 30, 30, light_gray),
            (60, 10, 25, 25, dark_gray),
            (5, 30, 25, 25, light_gray),
            (35, 35, 25, 25, dark_gray),
            (65, 40, 30, 30, light_gray),
            (10, 60, 20, 20, dark_gray),
            (40, 55, 30, 30, light_gray),
            (70, 65, 20, 20, dark_gray),
        ]

        for (x, y, w, h, color) in stones:
            pygame.draw.rect(surface, color, (x, y, w, h), border_radius=10)
        pygame.draw.rect(surface, COLOR.BLACK, (0, 0, 80, 80), 5)

        return surface
