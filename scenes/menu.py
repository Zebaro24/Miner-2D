import pygame

class Menu:
    def __init__(self, runner, width, height):
        self.runner = runner
        self.width = width
        self.height = height

        # Define colors
        self.text_color = (255, 255, 255)
        self.button_color = (100, 100, 100)
        self.button_hover_color = (150, 150, 150)
        self.input_active_color = (200, 200, 200)
        self.input_inactive_color = (100, 100, 100)

        # Define fonts
        self.title_font = pygame.font.Font(None, 74)
        self.font = pygame.font.Font(None, 36)

        # Input fields
        self.nickname = ""
        self.ip_address = ""

        # Buttons and input fields rectangles
        self.nickname_rect = pygame.Rect(width // 4, height // 3, width // 2, 50)
        self.play_button_rect = pygame.Rect(width // 4, height // 2, width // 2, 50)
        self.ip_address_rect = pygame.Rect(width // 4, 2 * height // 3, width // 2, 50)

        # Flags
        self.active_nickname = False
        self.active_ip = False

        # Load background image
        self.background_image = pygame.image.load(r"images\background1.png")
        self.bg_x = 0
        self.bg_speed = 1

    def draw(self, surface):
        # Move background
        self.bg_x -= self.bg_speed
        if self.bg_x <= -self.background_image.get_width():
            self.bg_x = 0

        # Draw background
        surface.blit(self.background_image, (self.bg_x, 0))
        surface.blit(self.background_image, (self.bg_x + self.background_image.get_width(), 0))

        # Draw title
        title_surf = self.title_font.render("Miner 2-D", True, self.text_color)
        title_rect = title_surf.get_rect(center=(self.width // 2, self.height // 6))
        surface.blit(title_surf, title_rect)

        # Draw nickname input
        nickname_color = self.input_active_color if self.active_nickname else self.input_inactive_color
        pygame.draw.rect(surface, nickname_color, self.nickname_rect, 2)
        nickname_surf = self.font.render(self.nickname, True, self.text_color)
        surface.blit(nickname_surf, (self.nickname_rect.x + 10, self.nickname_rect.y + 10))

        # Draw play button
        pygame.draw.rect(surface, self.button_color, self.play_button_rect)
        play_surf = self.font.render("Play", True, self.text_color)
        play_rect = play_surf.get_rect(center=self.play_button_rect.center)
        surface.blit(play_surf, play_rect)

        # Draw IP address input
        ip_color = self.input_active_color if self.active_ip else self.input_inactive_color
        pygame.draw.rect(surface, ip_color, self.ip_address_rect, 2)
        ip_surf = self.font.render(self.ip_address, True, self.text_color)
        surface.blit(ip_surf, (self.ip_address_rect.x + 10, self.ip_address_rect.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.nickname_rect.collidepoint(event.pos):
                self.active_nickname = True
                self.active_ip = False
            elif self.ip_address_rect.collidepoint(event.pos):
                self.active_ip = True
                self.active_nickname = False
            elif self.play_button_rect.collidepoint(event.pos):
                self.runner.set_menu_value(self.nickname, self.ip_address)
                self.runner.change_to_miner_2d()

        if event.type == pygame.KEYDOWN:
            if self.active_nickname:
                if event.key == pygame.K_BACKSPACE:
                    self.nickname = self.nickname[:-1]
                else:
                    self.nickname += event.unicode
            elif self.active_ip:
                if event.key == pygame.K_BACKSPACE:
                    self.ip_address = self.ip_address[:-1]
                else:
                    self.ip_address += event.unicode

        return None