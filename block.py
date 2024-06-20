from pygame import Surface


class Block:
    id = "id-block"

    @staticmethod
    def get_surface():
        surface = Surface((80, 80))
        return surface
