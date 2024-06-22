import pygame
from config import COLOR

from map_miner import MapMiner


class Miner2D:
    pygame.init()

    def __init__(self, runner, map_width, map_height):
        self.runner = runner
        self.map = MapMiner(map_width, map_height)
        self.map.generate_map()

        self.player_x, self.player_y = 2, 3

    def draw(self, screen: pygame.Surface):

        self.draw_map(screen)
        pygame.draw.rect(screen, (0, 0, 0), (0, 560, 880, 40))

    def draw_map(self, screen):
        screen.fill(COLOR.BACKGROUND)
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
    my_map = MapMiner(100, 100)
    my_map.generate_map()
    my_view_map = my_map.get_view_map(5, 5)
    for i in my_view_map:
        print(i)