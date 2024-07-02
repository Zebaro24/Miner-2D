from pygame import Surface
from pygame.image import load as pygame_image_load  # импортируем метод загрузки изображения

from blocks.block import Block  # Предполагается, что у вас есть свой класс Block
from config import COLOR


class Cobblestone(Block):
    id = "cobblestone"
    image_path = "images/cobblestone.png"
    time_destroy = 10