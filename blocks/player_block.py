from pygame.image import load as pygame_image_load  # импортируем метод загрузки изображения
from blocks.block import Block


class Player(Block):
    id = "player"
    image_path_player = "images/player/steve_face.png"

    def get_surface(self):
        if self.surface is None:
            self.surface = super().get_surface()
            image = pygame_image_load(self.image_path_player).convert_alpha()
            self.surface.blit(image, (0, 0))

        return self.surface
