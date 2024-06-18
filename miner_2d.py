import pygame

from blocks.cobblestone import Cobblestone


class Map(list):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super(Map, self).__init__()

        for i in range(height):
            self.append([None] * width)

    def generate_map(self):
        for y in range(self.height):
            for x in range(self.width):
                self[y][x] = self.generate_block()

    @staticmethod
    def generate_block():
        return Cobblestone


class Miner2D:
    pygame.init()

    def __init__(self, map_width, map_height):
        self.map = Map(map_width, map_height)
        self.map.generate_map()

    def draw(self, screen: pygame.Surface):
        screen.fill((255, 255, 255))

        self.draw_map(screen)

    def draw_map(self, screen):
        size = 80
        for y in range(7):
            for x in range(11):
                pygame.draw.rect(screen, (255, x*25, y*25), (size * x, size * y, size, size))
        pygame.draw.rect(screen, (0, 0, 0), (0, 560, 880, 40))


if __name__ == '__main__':
    # Miner2D().run()
    my_map = Map(10, 20)
    my_map.generate_map()
    print(my_map)
