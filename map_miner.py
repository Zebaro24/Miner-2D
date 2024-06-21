from typing import List, Optional
from random import choice

from pygame import Surface, SRCALPHA

from blocks.all_block import AllBlock
from blocks.block import Block


class MapMiner(list):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super(MapMiner, self).__init__()

        self.view_x = 7
        self.view_y = 5

        for _ in range(height):
            self.append([0] * width)

        self.all_block = AllBlock()

    def generate_map(self):
        for y in range(self.height):
            for x in range(self.width):
                self[y][x] = self.generate_block()

    def generate_block(self):
        list_blocks = self.all_block.get_list_block()
        return choice(list_blocks)

    def get_view_map(self, player_x, player_y):
        start_x, start_y = player_x - self.view_x, player_y - self.view_y
        full_view_x, full_view_y = self.view_x * 2 + 1, self.view_y * 2 + 1

        view_map: List[List[Optional[Block]]] = []
        for _ in range(self.view_y * 2 + 1):
            view_map.append([None] * (self.view_x * 2 + 1))

        for y in range(full_view_y):
            for x in range(full_view_x):
                x_abroad = start_x + x < 0 or start_x + x >= full_view_x
                y_abroad = start_y + y < 0 or start_y + y >= full_view_y

                if x_abroad or y_abroad:
                    view_map[y][x] = None
                else:
                    view_map[y][x] = self[start_y + y][start_x + x]

        return view_map

    def get_surface(self, player_x, player_y):
        surface = Surface((1200, 880), SRCALPHA)

        view_map = self.get_view_map(player_x, player_y)
        full_view_x, full_view_y = self.view_x * 2 + 1, self.view_y * 2 + 1
        for y in range(full_view_y):
            for x in range(full_view_x):
                view_block = view_map[y][x]
                if view_block is not None:
                    surface_block = view_block.get_surface()
                    surface.blit(surface_block, (x * 80, y * 80))

        return surface
