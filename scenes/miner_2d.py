import pygame
from random import randint
from config import COLOR

from map_miner import MapMiner
from player import Player
from scenes.inventory import Inventory


class Miner2D:
    pygame.init()

    def __init__(self, runner, map_width=100, map_height=100, map_miner=None):

        self.key = None
        self.player_x, self.player_y = 0, 0
        self.runner = runner
        if map_miner is None:
            print("map_miner is None")
            self.map = MapMiner(map_width, map_height)
            self.map.generate_map()

        self.set_player()
        self.done = False
        self.player = Player(runner.name)
        self.breaking = False
        self.speed = [0.0, 0.0]
        self.view_cord = [80 * (self.player_x + 1), 80 * (self.player_y + 1)]
        self.player_cord = self.view_cord.copy()
        print(self.view_cord)
        self.progress = 0
    def set_player(self):
        self.player_x, self.player_y = randint(40, self.map.width - 40), randint(40, self.map.height - 40)
        self.map.set_player_position(self.player_x, self.player_y)
        self.block = None
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
        if self.breaking:
            self.draw_breaking_block(screen)

    def draw_map(self, screen):
        self.player_cord = [80 * (self.player_x + 1), 80 * (self.player_y + 1)]
        self.move_view()
        screen.fill(COLOR.BACKGROUND)
        screen.blit(self.map.get_surface(self.player_x + 1, self.player_y + 1),
                    (self.player_cord[0] - self.view_cord[0] - 80, self.player_cord[1] - self.view_cord[1] - 80))

    def draw_balance(self, screen):
        pygame.draw.rect(screen, COLOR.BLACK, (0, 560, 880, 40))
        font = pygame.font.Font(None, 38)
        cobblestone_surface = font.render(f"Камінь: {self.player.count_cobblestone}", True, COLOR.WHITE)
        iron_surface = font.render(f"Железо: {self.player.count_iron}", True, COLOR.WHITE)
        gold_surface = font.render(f"Золото: {self.player.count_gold}", True, COLOR.WHITE)
        coordinate_surface = font.render(f"x{self.player_x} y{self.player_y}", True, COLOR.WHITE)
        token_surface = font.render(f"Токены: {self.player.count_tokens}", True, COLOR.YELLOW)

        screen.blit(cobblestone_surface, (20, 566))
        screen.blit(iron_surface, (220, 566))
        screen.blit(gold_surface, (500, 566))
        screen.blit(coordinate_surface, (25,25))
        screen.blit(token_surface, (700, 566))

    def exit_from_server(self):
        self.map.set_block(self.player_x, self.player_y, self.map.all_block.mycelium)
        self.map.send_changes()

    def move_player(self, event):
        if self.breaking:
            return


        if event.key == pygame.K_UP and self.player_y > 0:
            self.key = event.key
            self.block = self.map[self.player_y - 1][self.player_x]
            if self.block == self.map.all_block.mycelium:
                self.move_player_break()
            else:
                self.break_block(self.block)




        elif event.key == pygame.K_DOWN and self.player_y < 99:
            self.key = event.key
            self.block = self.map[self.player_y + 1][self.player_x]
            if self.block == self.map.all_block.mycelium:
                self.move_player_break()
            else:
                self.break_block(self.block)


        elif event.key == pygame.K_LEFT and self.player_x > 0:
            self.key = event.key
            self.block = self.map[self.player_y][self.player_x - 1]
            if self.block == self.map.all_block.mycelium:
                self.move_player_break()

            else:
                self.break_block(self.block)


        elif event.key == pygame.K_RIGHT and self.player_x < 99:
            self.key = event.key
            self.block = self.map[self.player_y][self.player_x + 1]
            if self.block == self.map.all_block.mycelium:
                self.move_player_break()
            else:
                self.break_block(self.block)






    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                self.move_player(event)
            elif event.key == pygame.K_e:
                if not self.runner.is_inventory:
                    self.runner.change_to_inventory()


            elif event.key == pygame.K_RETURN:
                self.player.convert_to_token()
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                self.breaking = False


    def break_block(self, block):
        self.done= False
        self.breaking = True
        self.progress = 0


    def draw_breaking_block(self, screen):
        pygame.draw.rect(screen, COLOR.BLACK, (100, 500, 600, 40))
        pygame.draw.rect(screen, COLOR.RED, (100, 500, self.progress, 40))
        self.progress += self.block.time_destroy/2
        if self.progress >= 600:
            self.done = True
            self.breaking = False
            self.progress = 0
            self.move_player_break()

    def move_player_break(self):
        if self.key == pygame.K_UP:
            self.map.set_block(self.player_x, self.player_y, self.map.all_block.mycelium)
            self.player_y -= 1
            self.map.all_block.player.set_up()
        elif self.key== pygame.K_DOWN:
            self.map.set_block(self.player_x, self.player_y, self.map.all_block.mycelium)
            self.player_y += 1
            self.map.all_block.player.set_down()
        elif self.key == pygame.K_LEFT:
            self.map.set_block(self.player_x, self.player_y, self.map.all_block.mycelium)
            self.player_x -= 1
            self.map.all_block.player.set_left()
        elif self.key == pygame.K_RIGHT:
            self.map.set_block(self.player_x, self.player_y, self.map.all_block.mycelium)
            self.player_x += 1
            self.map.all_block.player.set_right()
            # Перемещение блока добавлено внутрь условия self.done

        if self.block is self.map.all_block.iron_ore:
            self.player.add_iron()
        elif self.block is self.map.all_block.gold_ore:
            self.player.add_gold()
        elif self.block is self.map.all_block.cobblestone:
            self.player.add_cobblestone()

        self.map.set_block(self.player_x, self.player_y, self.map.all_block.player)
        self.map.send_changes()

if __name__ == '__main__':
    my_map = MapMiner(100, 100)
    my_map.generate_map()
    my_view_map = my_map.get_view_map(5, 5)
    for i in my_view_map:
        print(i)
