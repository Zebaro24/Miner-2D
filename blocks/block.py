from pygame import Surface


class Block:
    id = "id-block"
    surface = None

    def get_surface(self):
        if self.surface is None:
            self.surface = Surface((80, 80))
        return self.surface
