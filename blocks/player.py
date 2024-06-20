import pygame

from block import Block


class Player(Block):
    id = "player"
    image = pygame.image.load('cobblestone.png')

    @staticmethod
    def get_surface():
        surface = Surface((80, 80))


        return surface