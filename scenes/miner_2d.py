import pygame
from random import randint
from config import COLOR

from map_miner import MapMiner
from player import Player


class Miner2D:
    pygame.init()

    def __init__(self, runner, map_width=100, map_height=100, map_miner=None):
        self.player_x, self.player_y = 0, 0
        self.runner = runner
        if map_miner is None:
            print("map_miner is None")
            self.map = MapMiner(map_width, map_height)
            self.map.generate_map()

        self.set_player()

        self.player = Player(runner.name)

        self.speed = [0.0, 0.0]
        self.view_cord = [80 * (self.player_x + 1), 80 * (self.player_y + 1)]
        self.player_cord = self.view_cord.copy()
        print(self.view_cord)

    def set_player(self):
        self.player_x, self.player_y = randint(1, self.map.width - 2), randint(1, self.map.height - 2)
        self.map.set_player_position(self.player_x, self.player_y)

        print(self.player_x, self.player_y)

    def move_view(self):
        # <X>
        if self.view_cord[0] != self.player_cord[0]:
            self.speed[0] = (self.player_cord[0] - self.view_cord[0]) / 8
        else:
            self.speed[0] = 0

        # <Y>
        if self.view_cord[1] != self.player_cord[1]:
            self.speed[1] = (self.player_cord[1] - self.view_cord[1]) / 8
        else:
            self.speed[1] = 0

        self.view_cord[0] += self.speed[0]
        self.view_cord[1] += self.speed[1]

    def draw(self, screen: pygame.Surface):
        self.draw_map(screen)
        self.draw_balance(screen)

    def draw_map(self, screen):
        self.player_cord = [80 * (self.player_x + 1), 80 * (self.player_y + 1)]
        self.move_view()
        screen.fill(COLOR.BACKGROUND)
        screen.blit(self.map.get_surface(self.player_x + 1, self.player_y + 1),
                    (self.player_cord[0] - self.view_cord[0] - 80, self.player_cord[1] - self.view_cord[1] - 80))

    def draw_balance(self, screen):
        pygame.draw.rect(screen, COLOR.BLACK, (0, 560, 880, 40))
        font = pygame.font.Font(None, 38)
        iron_surface = font.render(f"Железо: {self.player.count_iron}", True, COLOR.WHITE)
        gold_surface = font.render(f"Золото: {self.player.count_gold}", True, COLOR.WHITE)
        coordinate_surface = font.render(f"x{self.player_x} y{self.player_y}", True, COLOR.WHITE)
        token_surface = font.render(f"Токены: {self.player.count_tokens}", True, COLOR.YELLOW)

        screen.blit(iron_surface, (20, 566))
        screen.blit(gold_surface, (220, 566))
        screen.blit(coordinate_surface, (500,566))
        screen.blit(token_surface, (700, 566))

    def exit_from_server(self):
        self.map.set_block(self.player_x, self.player_y, self.map.all_block.mycelium)
        self.map.send_changes()
    def move_player(self, event):
        self.map.set_block(self.player_x, self.player_y, self.map.all_block.mycelium)
        if event.key == pygame.K_UP and self.player_y>0:
            self.player_y -= 1
            self.map.all_block.player.set_up()

        elif event.key == pygame.K_DOWN and self.player_y<99:
            self.player_y += 1
            self.map.all_block.player.set_down()

        elif event.key == pygame.K_LEFT and self.player_x>0:
            self.player_x -= 1
            self.map.all_block.player.set_left()

        elif event.key == pygame.K_RIGHT and self.player_x<99:
            self.player_x += 1
            self.map.all_block.player.set_right()

        block = self.map[self.player_y][self.player_x]
        if block is self.map.all_block.iron_ore:
            self.player.add_iron()
        elif block is self.map.all_block.gold_ore:
            self.player.add_gold()

        self.map.set_block(self.player_x, self.player_y, self.map.all_block.player)
        self.map.send_changes()



    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                self.move_player(event)
            elif event.key == pygame.K_RETURN:
                self.player.convert_to_token()


if __name__ == '__main__':
    my_map = MapMiner(100, 100)
    my_map.generate_map()
    my_view_map = my_map.get_view_map(5, 5)
    for i in my_view_map:
        print(i)
