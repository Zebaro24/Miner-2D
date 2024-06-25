# runner.py
import pygame
from pygame.locals import QUIT
from scenes.menu import Menu
from scenes.miner_2d import Miner2D
from config import *
from sockets.client import Client


class Runner:
    def __init__(self, width, height, map_width, map_height):
        self.client = None
        self.draw = None
        self.handle_event = None
        self.run_bool = True

        self.name = None
        self.ip = None

        # name of window
        pygame.display.set_caption("Miner-2D")

        # for fps
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((width, height))

        self.menu = Menu(self, width, height)
        self.miner_2d = Miner2D(self, map_width, map_height)

        self.change_to_menu()

    def change_to_menu(self):
        self.draw = self.menu.draw
        self.handle_event = self.menu.handle_event

    def change_to_miner_2d_from_menu(self):
        self.draw = self.miner_2d.draw
        self.handle_event = self.miner_2d.handle_event

    def set_menu_value(self, name, ip):
        self.name = name
        self.ip = ip

    def new_client(self, ip):
        self.client = Client(ip, self.miner_2d)
        self.client.start()

    def run(self):
        while self.run_bool:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run_bool = False
                    if self.client:
                        self.client.close_connection()
                else:
                    self.handle_event(event)

            self.draw(self.screen)

            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()


if __name__ == '__main__':
    runner = Runner(WINDOW_WIDTH, WINDOW_HEIGHT, MAP_WIDTH, MAP_HEIGHT)
    runner.run()
