from pygame import Surface
from pygame.image import load as pygame_image_load  # импортируем метод загрузки изображения

from blocks.block import Block  # Предполагается, что у вас есть свой класс Block
from config import COLOR


class GoldOre(Block):
    id = "gold_ore"
    image_path = "images/gold_ore.png"
    time_destroy = 1