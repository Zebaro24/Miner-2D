from pygame import Surface
from pygame.image import load as pygame_image_load  # импортируем метод загрузки изображения

from blocks.block import Block  # Предполагается, что у вас есть свой класс Block
from config import COLOR


class Cobblestone(Block):
    id = "cobblestone"

    def get_surface(self):
        if self.surface is None:
            image_path = 'images/cobblestone.png'
            image = pygame_image_load(image_path).convert_alpha()

            self.surface = Surface(image.get_size())
            self.surface.fill(COLOR.BACKGROUND)

            self.surface.blit(image, (0, 0))
        return self.surface
