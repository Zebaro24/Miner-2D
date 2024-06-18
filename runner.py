from miner_2d import Miner2D

from config import *

from pygame.locals import QUIT, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP
import pygame


class Runner:
    def __init__(self, width, height, map_width, map_height):
        self.run_bool = True

        # name of window
        pygame.display.set_caption("Miner-2D")

        # for fps
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))

        self.miner_2d = Miner2D(map_width, map_height)

        self.draw = self.miner_2d.draw

    def run(self):
        while self.run_bool:
            # to detect some events
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.run_bool = False

                # mouse motion
                if event.type == MOUSEMOTION:
                    # self.mouse_motion(event.pos)
                    pass

                # if clicked
                if event.type == MOUSEBUTTONDOWN:
                    # self.mouse_clicked(event.button)
                    pass

                # if un clicked
                elif event.type == MOUSEBUTTONUP:
                    # self.mouse_un_clicked(event.button)
                    pass

                if event.type == pygame.KEYDOWN:
                    # self.key_clicked(event.key)
                    pass

            self.draw(self.screen)

            # self.tics()

            pygame.display.update()
            # fps on screen
            self.clock.tick(60)

        pygame.quit()


if __name__ == '__main__':
    runner = Runner(WINDOW_WIDTH, WINDOW_HEIGHT, MAP_WIDTH, MAP_HEIGHT)
    runner.run()
