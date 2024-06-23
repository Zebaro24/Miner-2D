from pygame import Surface
from pygame.image import load as pygame_image_load  # импортируем метод загрузки изображения
from config import COLOR


class Block:
    id = "id-block"
    image_path = "images/mycelium_top.png"
    surface = None

    def get_surface(self):
        if self.surface is None:
            image = pygame_image_load(self.image_path).convert_alpha()

            self.surface = Surface(image.get_size())
            self.surface.fill(COLOR.BACKGROUND)

            self.surface.blit(image, (0, 0))
        return self.surface
