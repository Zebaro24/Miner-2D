import pygame
import sys

class Inventory:
    def __init__(self, runner, width, height):
        print("Inventory init")
        self.runner = runner
        self.width = width
        self.height = height

        # Define colors
        self.text_color = (255, 255, 255)
        self.button_color = (100, 100, 100)
        self.button_hover_color = (150, 150, 150)
        self.input_active_color = (200, 200, 200)
        self.input_inactive_color = (100, 100, 100)
        self.bg_color = (50, 50, 50)

        self.font = pygame.font.Font(None, 36)

        # Load images
        self.image_paths = [
            "images/items/wood_pickaxe.png",
            "images/items/stone_pickaxe.png",
            "images/items/iron_pickaxe.png",
            "images/items/gold_pickaxe.png",
            "images/items/diamond_pickaxe.png"
        ]
        self.images = [pygame.transform.scale(pygame.image.load(path), (80, 80)) for path in self.image_paths]

        # Item details
        self.items = [
            {"level": 1,"rect": pygame.Rect(50, 150 + 0 * 120, 800, 100), "text": f"Item wood pickaxe", "price": "100$", "image": self.images[0]},
            {"level": 2,"rect": pygame.Rect(50, 150 + 1 * 120, 800, 100), "text": f"Item stone pickaxe", "price": "500$", "image": self.images[1]},
            {"level": 3,"rect": pygame.Rect(50, 150 + 2 * 120, 800, 100), "text": f"Item iron pickaxe", "price": "1500$", "image": self.images[2]},
            {"level": 4,"rect": pygame.Rect(50, 150 + 3 * 120, 800, 100), "text": f"Item gold pickaxe", "price": "3000$", "image": self.images[3]},
            {"level": 5,"rect": pygame.Rect(50, 150 + 4 * 120, 800, 100), "text": f"Item diamond pickaxe", "price": "5000$", "image": self.images[4]},

        ]

        self.scroll_offset = 0
        self.scroll_speed = 20
        total_content_height = self.items[-1]["rect"].bottom - self.items[0]["rect"].top
        self.max_scroll_offset = max(0, total_content_height - self.height)

        # Устанавливаем начальное смещение прокрутки
        self.scroll_offset = 0
    def draw(self, surface):
        surface.fill(self.bg_color)

        # Draw items
        for item in self.items:
            item_rect = item["rect"].move(0, -self.scroll_offset)
            balance = self.runner.miner_2d.player.count_tokens

            can_buy = balance >= int(item["price"].replace("$", ""))
            if can_buy:

                item_color = self.input_active_color
            else:

                item_color = self.input_inactive_color

            if item_rect.colliderect(surface.get_rect()):
                pygame.draw.rect(surface, item_color, item_rect)
                surface.blit(item["image"], (item_rect.x + 10, item_rect.y + 10))
                text_surf = self.font.render(item["text"], True, self.text_color)
                price_surf = self.font.render(item["price"], True, self.text_color)
                surface.blit(text_surf, (item_rect.x + 100, item_rect.y + 30))
                surface.blit(price_surf, (item_rect.x + 600, item_rect.y + 30))

        # Draw title
        title_rect = pygame.Rect(0, 0, self.width, 150)
        pygame.draw.rect(surface, self.bg_color, title_rect)
        title_surf = self.font.render("shop", True, self.text_color)
        title_rect = title_surf.get_rect(center=title_rect.center)
        surface.blit(title_surf, title_rect)
        self.runner.miner_2d.draw_balance(surface)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click

            for i, item in enumerate(self.items):
                item_rect = item["rect"].move(0, -self.scroll_offset)

                if item_rect.collidepoint(event.pos):
                    balance = self.runner.miner_2d.player.count_tokens
                    required_balance = int(item["price"].replace("$", ""))
                    if balance >= required_balance:

                        # перевіряємо, чи не купує гравець кірку гіршу, за ту шо в нього є
                        if self.runner.miner_2d.player.item['level'] < item["level"]:
                            if self.runner.miner_2d.player.item['level']+1 == item["level"]:

                                self.runner.miner_2d.player.count_tokens = balance - required_balance
                                self.runner.miner_2d.player.item["level"] = item['level']
                                self.runner.miner_2d.player.item["item"] = item['text']
                                print(f"{item['text']} clicked")
                                break
                            else:
                                lvl = item['level'] - 1
                                for item in self.items:
                                    if item["level"] == lvl:
                                        print(f"сначала купите {item['text']} kirku")
                        # якшо гірше, то не купуємо
                        else:
                            print("Y вас круче")

        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:  # крутим вверх
                self.scroll_offset = max(0, self.scroll_offset - self.scroll_speed)
            elif event.y < 0:  # крутим вниз
                self.scroll_offset = min(200, self.scroll_offset + self.scroll_speed)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                self.runner.is_inventory = False
                self.runner.change_to_miner_2d_from_menu()

        return None

# Example runner class for context
class Runner:
    def __init__(self):
        self.is_inventory = True

    def change_to_miner_2d_from_menu(self):
        print("Change to miner 2D from menu")

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Inventory Example")
    clock = pygame.time.Clock()

    runner = Runner()
    inventory = Inventory(runner, 800, 600)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            inventory.handle_event(event)

        inventory.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
