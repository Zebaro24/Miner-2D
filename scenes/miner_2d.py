import pygame
from pygame import Surface

from blocks.cobblestone import Cobblestone


class Map(list):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        super(Map, self).__init__()

        self.view_x = 7
        self.view_y = 5

        for i in range(height):
            self.append([0] * width)

    def generate_map(self):
        for y in range(self.height):
            for x in range(self.width):
                self[y][x] = self.generate_block()

    @staticmethod
    def generate_block():
        return Cobblestone

    def get_view_map(self, player_x, player_y):
        start_x, start_y = player_x - self.view_x, player_y - self.view_y
        full_view_x, full_view_y = self.view_x * 2 + 1, self.view_y * 2 + 1

        view_map = []
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
        surface = Surface((1200, 880), pygame.SRCALPHA)

        view_map = self.get_view_map(player_x, player_y)
        full_view_x, full_view_y = self.view_x * 2 + 1, self.view_y * 2 + 1
        for y in range(full_view_y):
            for x in range(full_view_x):
                if view_map[y][x]:
                    surface_block = view_map[y][x].get_surface()
                    surface.blit(surface_block, (x * 80, y * 80))
        return surface


class Miner2D:
    pygame.init()

    def __init__(self, runner, map_width, map_height):
        self.runner = runner
        self.map = Map(map_width, map_height)
        self.map.generate_map()

        self.player_x, self.player_y = 2, 3

    def draw(self, screen: pygame.Surface):

        self.draw_map(screen)
        pygame.draw.rect(screen, (0, 0, 0), (0, 560, 880, 40))

    def draw_map(self, screen):
        screen.fill((43, 45, 48))
        screen.blit(self.map.get_surface(self.player_x + 1, self.player_y + 1), (-80, -80))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.player_y -= 1

            elif event.key == pygame.K_DOWN:
                self.player_y += 1

            elif event.key == pygame.K_LEFT:
                self.player_x -= 1

            elif event.key == pygame.K_RIGHT:
                self.player_x += 1


if __name__ == '__main__':
    # Miner2D().run()
    my_map = Map(100, 100)
    my_map.generate_map()
    my_view_map = my_map.get_view_map(5, 5)
    for i in my_view_map:
        print(i)
