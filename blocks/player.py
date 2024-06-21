from pygame import Surface

from blocks.block import Block


class Player(Block):
    id = "player"

    def get_surface(self):
        if self.surface is None:
            self.surface = Surface((80, 80))
        return self.surface
