import pygame
from random import randint
from config import COLOR

from map_miner import MapMiner


class Miner2D:
    pygame.init()

    def __init__(self, runner, map_width, map_height):
        self.runner = runner
        self.map = MapMiner(map_width, map_height)
        self.map.generate_map()

        self.player_x, self.player_y = randint(1, 8), randint(1, 8)
        self.map.set_player_position(self.player_x, self.player_y)
        print(self.player_x, self.player_y)

    def draw(self, screen: pygame.Surface):

        self.draw_map(screen)
        pygame.draw.rect(screen, (0, 0, 0), (0, 560, 880, 40))

    def draw_map(self, screen):
        screen.fill(COLOR.BACKGROUND)
        screen.blit(self.map.get_surface(self.player_x + 1, self.player_y + 1), (-80, -80))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.map.set_block(self.player_x, self.player_y, self.map.all_block.mycelium)
            if event.key == pygame.K_UP:
                self.player_y -= 1

            elif event.key == pygame.K_DOWN:
                self.player_y += 1

            elif event.key == pygame.K_LEFT:
                self.player_x -= 1

            elif event.key == pygame.K_RIGHT:
                self.player_x += 1

            self.map.set_block(self.player_x, self.player_y, self.map.all_block.player)


if __name__ == '__main__':
    my_map = MapMiner(100, 100)
    my_map.generate_map()
    my_view_map = my_map.get_view_map(5, 5)
    for i in my_view_map:
        print(i)
