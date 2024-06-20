import pygame
from pygame import Surface
from pygame.image import load as pygame_image_load  # импортируем метод загрузки изображения

from block import Block  # Предполагается, что у вас есть свой класс Block
from config import COLOR

class Cobblestone(Block):
    id = "cobblestone"

    @staticmethod
    def get_surface():
        # Загружаем изображение
        image_path = 'images/cobblestone.png'
        image = pygame_image_load(image_path).convert_alpha()


        surface = Surface(image.get_size())
        surface.fill(COLOR.BACKGROUND)

        surface.blit(image, (0, 0))

        return surface
