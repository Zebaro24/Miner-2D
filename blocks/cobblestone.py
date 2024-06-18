from block import Block


class Cobblestone(Block):
    id = "cobblestone"

    # def get_surface(self):
    #     for _ in range(20):  # 20 камней
    #         # Случайный размер камня
    #         stone_size = random.randint(5, 15)
    #         # Случайная позиция камня внутри блока
    #         stone_x = random.randint(0, block_size - stone_size)
    #         stone_y = random.randint(0, block_size - stone_size)
    #         # Случайный цвет камня (от темного до светлого серого)
    #         stone_color = (random.randint(105, 140), random.randint(105, 140), random.randint(105, 140))
    #         # Рисуем камень (круг)
    #         pygame.draw.ellipse(surface, stone_color, (stone_x, stone_y, stone_size, stone_size))
    #     return